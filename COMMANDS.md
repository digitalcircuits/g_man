Run any of these commands, and the most recently posted video will be edited. Videos can be a link (youtube, twitter, and discord supported) or a direct upload.

Some commands may be listed as having multiple names, this means they are the same command.<br>
Example: `!saturate 5` is the same as `!saturation 5`<br><br>

# Bitrate
| Command | Format | Min/Max Values | Description | Examples |
| --- | --- | --- | --- | --- |
| vb | `!vb <bitrate>` | `8000 to 200000` | Set the video bitrate. | `!vb 30000` |
| ab | `!ab <bitrate>` | `8000 to 200000` | Set the audio bitrate. | `!ab 50000` |
| b | `!b <video_bitrate> <audio_bitrate>` | video_bitrate: `8000 to 200000`<br>audio_bitrate: `8000 to 200000` | Set the video and audio bitrate. | `!b 30000 50000` |
<br>

# Filters
| Command | Format | Min/Max Values | Description | Examples |
| --- | --- | --- | --- | --- |
| amplify | `!amplify <amount> <radius>` | amount: `0 to 65535`<br><br>radius: `1 to 63` | Makes pixels more colorful the more they change. A higher \<amount\> makes the pixels more colorful, with a default value of 6.<br><br>OPTIONAL: \<radius\> determines how many adjacent frames each frame looks at to consider how much a pixel has changed by. By default the value is 1.<br><br>NOTE: a higher \<radius\> causes more frames to drop at the start and end of the video. | `!amplify 15`<br><br>`!amplify 15 30`
| audioblend<br>audiomerge | `!audioblend` | | Blend the audio in the second to most recent video with the audio from the most recent video. | `!audioblend` |
| audioswap | `!audioswap` | | Swap the audio in the second to most recent video with the audio from the most recent video. | `!audioswap` |
| backwards | `!backwards` | | Reverse the video. | `!backwards` |
| blur | `!blur <amount>` | `1 - 127` | Blur the video. \<amount\> represents the radius of the blur around each pixel. | `!blur 10` |
| brightness | `!brightness <amount>` | `-1 to 1` | Adjust the brightness of a video. | `!brightness 2` |
| concat<br>merge | `!concat` | | Combine the two most recently sent videos. Most recent video will be played after the second to most recent. | `!concat` |
| contrast | `!contrast <amount>` | `-1000 to 1000` | Change the video's contrast. | `!contrast 2` |
| edges | `!edges` | | Show only the edges in the video. | `!edges` |
| equalize<br>equalizer | `!equalize <b1> <b2> ... <b17> <b18>` | `0 to inf` | 18 band equalizer. More information here: https://ffmpeg.org/ffmpeg-filters.html#superequalizer<br>You can provide a number for each frequency band. If you don't provide a value, or set a value as -1, it is set to a random number between 0 and 20. | `!equalize 10 10 -1 5 5 0 0` |
| extract | `!extract <start_time> <end_time>`<br><br>`!extract <duration>` | | Extract the clip between \<start_time\> and \<end_time\>. Time can be specified in seconds (ex: `5` or `7.1`) or minutes:seconds (ex: `0:03` or `1:24.8`). You can also use `start` or `end` to specify the start or end of the video.<br><br>You can also use just one number as a `<duration>` to extract from the start of the video, meaning `!extract 0 1:15` is the same as `!extract 1:15`. | `!extract 3 5.5`<br><br>`!extract 1:15 1:30`<br><br>`!extract 10 end`<br><br>`!extract 5` |
| fps | `!fps <framerate>` | `1 to 60` | Set the framerate of the video. | `!fps 15` |
| gamma | `!gamma <amount>` | `0.1 to 10` | Change the video's gamma. | `!gamma 1.2` |
| hue | `!hue <degrees>` | `-inf to inf` | Change the video's hue. | `!hue 180` |
| invert<br>inverse<br>negate<br>negative | `!invert` | | Invert the video's colors. | `!invert` |
| lagfun | `!lagfun <amount>` | `0 to 1` | Makes darker pixels update slower. This can create an interesting smearing effect with lighter pixels. A higher \<amount\> makes the smearing last longer, with a value of 1 causing bright colors to never disappear. Values close to 0.96 create very noticable results. | `!lagfun 0.99` |
| loop | `!loop <amount>` | `2 to 20` | Loop the video. | `!loop 5` |
| saturate<br>saturation | `!saturate <amount>` | `-10 to 10` | Saturate the video. | `!saturate 2` |
| scale | `!scale <width> <height>` | `50 to 1240` | Scale the video. You can maintain aspect ratio by setting \<width\> or \<height\> to auto. By default, \<width\>=360 and \<height\>=270. | `!scale 640 auto` |
| speed | `!speed <amount>` | `0.05 to inf` | Change the speed of the video. | `!speed 2` |
| volume | `!volume <amount>` | `-inf to inf` | Increase/decrease volume. A value of 1 does no change. | `!volume 5` |
| wobble | `!wobble <frequency>` | `More than 0` | Make the audio wobbly. | `!wobble 15` |
<br>

# Corruption
| Command | Format | Min/Max Values | Description | Examples |
| --- | --- | --- | --- | --- |
| corrupt | `!corrupt <intensity>` | `0 to 1` | Set random bytes in the video file to a random number. | `!corrupt 0.7` |
| mosh | `!mosh <max_iframe_interval> <qmin>` | max_iframe_interval: `2 to inf`<br> | Datamosh the video. Maximum distance between iframes can be set with `<max_iframe_interval>`, by default it's 30| `!mosh`<br><br>`!mosh 15` |
| rearrange | `!rearrange <intensity>` | `0 to 1` | Swap random chunks of bytes in the video. A higher \<intensity\> does more swaps and makes the chunks longer. | `!rearrange 0.4` |
| smear | `!smear` | | Makes a cool smearing effect, using `tomato.py`. | `!smear` |
| stutter | `!stutter` | | Repeats random chunks of bytes back-to-back in various places. A bit like `!smear`, but not as smooth. | `!stutter` |
<br>

# Fun effects
| Command | Format | Min/Max Values | Description | Examples |
| --- | --- | --- | --- | --- |
| americ | `!americ` | | Replaces the video's audio with "Never Meant" by American Football. | `!americ` |
| cartoony<br>cartoon | `!cartoony` | | Makes the video look more cartoony. | `!cartoony` |
| demonize | `!demonize` | | Makes the video look and sound more scary. | `!demonize` |
| histogram | `!histogram` | | Convert the video into a histogram of the audio volume. | `!volume` |
| hypercam | `!hypercam` | | Add an Unregistered Hypercam 2 watermark. | `!hypercam` |
| ifunny | `!ifunny` | | Add an iFunny watermark. | `!ifunny` |
| mp3 | `!mp3` | | Convert video to an mp3. | `!mp3`|
| pingpong | `!pingpong` | | Plays the video, then plays it in reverse. | `!pingpong` |
| rainbow | `!rainbow <speed>` | `-inf to inf` | Makes the hue change over time, creating a rainbow effect. By default it's 360 degrees per second, you can multiply this speed by \<speed\>. | `!rainbow`<br><br>`!rainbow 2` |
| text | `!text <top_text>\|<bottom_text>` | | Adds captions to the top and bottom of the video. You separate \<top_text\> and \<bottom_text\> with a pipe symbol `\|`. | `!text this will be on top\|and this will be on the bottom`<br><br>`!text this will only be on top`<br><br>`!text \|this will only be on the bottom` |
| tutorial | `!tutorial <top_text>\|<bottom_text>` | | Converts the video into an old-school YouTube tutorial made with Windows Movie Maker. You can customize the title screen's \<top_text\> and \<bottom_text\> the same way you would with the !text command. If no top text is provided, a randomized title is chosen. If no bottom text is provided, "By your_username" is chosen. | `!tutorial how to download google chrome\|working 2010` |
<br>

# Advanced
## !filter command
You can apply almost any filter from FFMPEG using the !filter command.<br>
* Format: `!filter <filter_name> <filter_args>`
* \<filter_args\> are formatted in this way: `arg1_name=arg1_value arg2_name=arg2_value ...`
* Examples:
    * `!filter aecho`
    * `!filter edgedetect low=0.1 mode=wires`
    * `!filter drawtext text="g_man was here" x="(main_w-tw)/2" y="(main_h-th)/2 + 100*sin(t*6)" fontsize=50`
* Multiple filters can be applied with one message by simply appending another `!filter <filter_name> <filter_args>`
* Examples:
    * `!filter reverse !filter areverse`
    * `!filter eq contrast=1.2 !filter hue h=60 enable=gte(t,3) !filter negate`
