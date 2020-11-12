import traceback
import ffmpeg
import discord
import os
import image_cache

class TimeoutError(Exception):
    pass
def interrupt(a,b):
    raise TimeoutError

loading_emotes = [
    '\U0001F1EC',
    '\U0001F1F2',
    '\U0001F1E6',
    '\U0001F1F3'
]
async def set_progress_bar(ctx, idx):
    await ctx.message.add_reaction(loading_emotes[idx])

# Download the video, then wrap the filter code in a try catch statement
async def apply_filters_and_send(ctx, code, kwargs):
    #await ctx.message.add_reaction('\U0001F4AC')
    await set_progress_bar(ctx, 0)
    input_vid, is_yt, result = await image_cache.download_last_video(ctx)
    if(not result):
        await ctx.send("Error downloading the video")
        return
    await set_progress_bar(ctx, 1)

    output_filename = f'vids/{ctx.message.id}.mp4'
    
    async with ctx.typing():
        try:
            input_stream = ffmpeg.input(input_vid)
            input_stream_v, input_stream_a, output_params = await code(ctx, input_stream.video, input_stream.audio, kwargs)
            if('fs' not in output_params):
                output_params['fs'] = '7M'
            await set_progress_bar(ctx, 2)
            (
                ffmpeg
                .output(input_stream_a, input_stream_v, output_filename, **output_params)
                .run(cmd='ffmpeg4-2-2/ffmpeg', overwrite_output=True)
            )
            await set_progress_bar(ctx, 3)
            await ctx.send(file=discord.File(output_filename))
        except TimeoutError as e:
            await ctx.send(f'Command took to long to execute.\n```\n{str(e)}```')
        except Exception as e:
            await ctx.send(f'Error:\n```\n{str(e)}```')
            print(traceback.format_exc())

        # Remove files
        try:
            if(os.path.isfile(output_filename)):
                os.remove(output_filename)
        except Exception as e:
            print(e)
        try:
            if(is_yt):
                os.remove(input_vid)
        except Exception as e:
            print(e)
        await ctx.message.clear_reactions()


# Convert corrupted video to mp4
# Very repetitive, maybe there's a way to combine the two wrappers
async def apply_corruption_and_send(ctx, code, kwargs):
    await set_progress_bar(ctx, 0)
    input_vid, is_yt, result = await image_cache.download_last_video(ctx)
    if(not result):
        await ctx.send("Error downloading the video")
        return
    await set_progress_bar(ctx, 1)

    avi_filename = f'vids/{ctx.message.id}.avi'
    output_filename = f'vids/{ctx.message.id}.mp4'
    
    async with ctx.typing():
        try:
            (
                ffmpeg
                .input(input_vid)
                .output(avi_filename, fs='7M')
                .run(cmd='ffmpeg4-2-2/ffmpeg', overwrite_output=True)
            )

            successful_corrupt = True
            try:
                await code(ctx, avi_filename, kwargs)
                await set_progress_bar(ctx, 2)
            except Exception as e:
                await ctx.send(f'Error while corrupting the video: {e}')
                print(e)
                successful_corrupt = False

            if(successful_corrupt):
                (
                    ffmpeg
                    .input(avi_filename)
                    .output(output_filename, fs='7M')
                    .run(cmd='ffmpeg4-2-2/ffmpeg', overwrite_output=True)
                )
                await set_progress_bar(ctx, 3)
                await ctx.send(file=discord.File(output_filename))
        except TimeoutError as e:
            await ctx.send(f'Command took to long to execute.\n```\n{str(e)}```')
        except Exception as e:
            await ctx.send(f'Error:\n```\n{str(e)}```')
            print(traceback.format_exc())

        # Remove files
        try:
            if(os.path.isfile(avi_filename)):
                os.remove(avi_filename)
        except Exception as e:
            print(e)
        try:
            if(os.path.isfile(output_filename)):
                os.remove(output_filename)
        except Exception as e:
            print(e)
        try:
            os.remove(input_vid)
        except Exception as e:
            print(e)
        await ctx.message.clear_reactions()

    