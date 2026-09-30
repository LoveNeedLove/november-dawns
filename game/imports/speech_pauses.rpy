
###############################################################################################################
### RENPY SPEECH PAUSES #######################################################################################
###############################################################################################################
#
# Thanks for downloading my Automatic Speech Pauses plugin for Ren'Py! ( https://brunoais.itch.io/renpy-speech-pauses )
#
# Now, all you need to do is adjust the pause lengths below to your liking and (optionally) add new settings to
# your preferences screen to leave the choice up to the player!
#
# If you like this tool, consider dropping a donation: https://github.com/sponsors/brunoais?frequency=one-time
# Credit to "brunoais" and "KigyoDev" (the original author) would also be appreciated!
# "KigyoDev"'s version can be accessed here: https://kigyo.itch.io/speech-pauses-for-renpy
#
# Credit is due to KigyoDev for the initial idea and solution which allowed me to make this version much more
# easily. Also for accepting me copying the way he formats comments to make this tool more understandable for you.
# Without his work, I wouldn't have done this. Specially not this easily and fast. Thank you.
#
# Thank you and have fun! :D
# - Brunoais
#
###############################################################################################################



############################################# Configuration ###################################################
#  You can edit the content here to your liking
##################################################


####
## Default values
init -50:

    ###
    # These default values set for the first time. Once they are stored, editing these in this file doesn't make effect.
    # Because they are stored in `persistent`. They are set once and last "forever".
    #
    # Note: After running once, changing these values won't take any effect.
    #       However, you can temporarily test and tune them, by replacing `default` with `$`, but remember to undo that later.
    # Warning: if "Text speed" setting is maxed, relative pauses have no effect because the pausing time will be effectively 0.
    ##

    # Setting for user:
    # Toggle whether speech pauses are active
    # default value: True
    default persistent._brunoais__speech_pauses_enabled = True

    # Setting for user:
    # The pause duration of commas and ellipses in seconds
    # Whether the "_relative" or non relative is used is based on "_relative_enabled"
    # Values here are converted to mean the duration of the pause in seconds
    default persistent._brunoais__speech_pause_comma = 0.2
    default persistent._brunoais__speech_pause_comma_relative = 0.3
    # Whether to use the "_relative" variant or absolute variant for calculation
    default persistent._brunoais__speech_pause_comma_relative_enabled = True


    # Setting for user:
    # The pause duration of  periods, question marks, em dashes, and so on
    # Whether the "_relative" or non relative is used is based on "_relative_enabled"
    # Values here are converted to mean the duration of the pause in seconds
    default persistent._brunoais__speech_pause_period = 0.3
    default persistent._brunoais__speech_pause_period_relative = 0.4
    # Whether to use the "_relative" variant or absolute variant for calculation
    default persistent._brunoais__speech_pause_period_relative_enabled = True


## If you want to temporarily override those user options above during the VN play, just set these along the script as appropriate:
# speechPauses.enabled
# speechPauses.pause_comma_override
# speechPauses.pause_period_override
#
## (Those three values are defined more down below in the Definitions section)
#
## E.g.
# label partOfMyScript:
#     from store import speechPauses
#
#     # Override period user setting with relative wait time.
#     $ speechPauses.pause_period_override = "*0.4"
#     e "MUAHAHAHAH!!!!!! Hear my rage!!!"
#     "Slower!"
#
#     $ speechPauses.pause_period_override = "0.6"
#     e "MUAHAHAHAH!!!!!! Hear my rage!!!"
#     "Too slow! I'll do it myself!"
#
#     # Turn off automatic pauses
#     $ speechPauses.enabled = False
#     e "MUAHAHAHAH!!!!!{w=1}!{w=1} Hear my rage!!{w=1}!"
#     "Now THAT's more like it."
#
#     # Reset back to normal
#     $ speechPauses.enabled = None
#     $ speechPauses.pause_period_override = None
#


## Default screen ################################################################################################

# This is a screen you can use directly from your code.
# It allows users to customize the preferences above.
# You may just include it as-is in your settings. For example:
#
# use brunoais__speech_pause()
#
##
# If the animation doesn't play right (E.g. Finishes before collapsing), you can specify different sizes to make it work. For example:
# use brunoais__speech_pause(checkbox_height=120, two_bars_height=300)
##
# checkbox_height: The height that the checkboxes take on screen.
# two_bars_height: The height that two bars take on screen.
##
# Or you can copy and modify it however you want for your VN.
#


screen brunoais__speech_pause(style_prefix_=None, checkbox_height=90, two_bars_height=150):

    if style_prefix_ is not None:
        style_prefix style_prefix_

    # Be kind, if the user decides to just type: brunoais__speech_pause(None, None, 120)
    if checkbox_height is None:
        $ checkbox_height = 90

    vbox:
        vbox:

            #
            # Toggle Speech Pauses feature
            #
            label _("Speech Pauses")
            style_prefix "check"
            textbutton _("Speech Pauses") action ToggleField(persistent,"_brunoais__speech_pauses_enabled")

        showif persistent._brunoais__speech_pauses_enabled:
            hbox at brunoais__speech_pause_expander(checkbox_height):
                box_wrap True
                style_prefix "radio"
                textbutton _("Relative pauses") action (
                        SetField(persistent,"_brunoais__speech_pause_comma_relative_enabled", True),
                        SetField(persistent,"_brunoais__speech_pause_period_relative_enabled", True)
                    )
                textbutton _("Absolute pauses") action (
                        SetField(persistent,"_brunoais__speech_pause_comma_relative_enabled", False),
                        SetField(persistent,"_brunoais__speech_pause_period_relative_enabled", False)
                    )

            fixed at brunoais__speech_pause_expander(two_bars_height):
                yfit True
                showif persistent._brunoais__speech_pause_comma_relative_enabled:
                    vbox:
                        style_prefix "slider"
                        label _("Commas")
                        bar value FieldValue(persistent, "_brunoais__speech_pause_comma_relative", step=.05, style=u'slider', offset=0.05, range=0.95)
                        label _("Sentences")
                        bar value FieldValue(persistent, "_brunoais__speech_pause_period_relative", step=.05, style=u'slider', offset=0.1, range=1.9)
                        showif preferences.text_cps == 0.0:
                            label _("{color=ff0000}When Text Speed is maxed out, relative pauses have no effect")
                else:
                    vbox:
                        style_prefix "slider"
                        label _("Commas")
                        bar value FieldValue(persistent, "_brunoais__speech_pause_comma", step=.05, style=u'slider', offset=0.05, range=0.95)
                        label _("Sentences")
                        bar value FieldValue(persistent, "_brunoais__speech_pause_period", step=.05, style=u'slider', offset=0.1, range=1.9)

transform brunoais__speech_pause_expander(y=90):
    on show:
        alpha 0 yoffset -y
        easein 0.3 alpha 1 yoffset 0
    on hide:
        alpha 1 yoffset 0
        easein 0.3 alpha 0 yoffset -y


############################################# Definitions ###################################################
#  You can edit the content here to your needs
#  If you edit anything here that may add value to the tool itself, I'd be glad if you contribute back to the tool by making a new post at:
#  https://brunoais.itch.io/renpy-speech-pauses/community
##################################################

init -10 python in speechPauses:

    # None means to use the value of preferences._brunoais__speech_pauses_enabled
    # Overrides preferences._brunoais__speech_pauses_enabled which may be set by the user.
    # Use this only when it's really meaningful or impactful!
    enabled = None

    # Define what counts as a "comma" (shorter pause)
    # default value: [",", "...", "，","、", "…", "——"]
    speech_comma = [",", "...", "，","、", "…", "——"]

    # Define what counts as a "period" (longer pause)
    # default value: [".", "?", "!", ":", ";", "—", "~", "。", "？", "！", "；", "：", "……"]
    speech_period = [".", "?", "!?", "!", "!!!", ":", ";", "—", "~", "。", "？", "！", "；", "：", "……"]


    ###
    ## Define exceptions where any of the above symbols should not lead to a pause.
    ## Exceptions are organized by language because different languages have different needs.
    ## Having it organized like this helps accomodating to the different languages out-of-the-box.
    ###

    # For English language
    en_speech_exceptions = ["Mr.", "Ms.", "Mrs.", "Dr."]

    # For Japanese language
    jp_speech_exceptions = []

    # For Spanish language
    es_speech_exceptions = ["Sr.", "Sra.", "Dr.", "Dra."]

    ## More languages later based on volunteering from public.
    # _speech_exceptions = []
    ##

    # For Indonesian language (Credit: namoniya: https://itch.io/t/4752178/indonesian-language-submission)
    id_speech_exceptions = ["Tn.", "Ny." "dr.", "Dr."]


    # Consider english the default language. So default to english speech exceptions.
    speech_exceptions = en_speech_exceptions


translate None python:
    ##########
    # If your VN's default language is not english change this value.
    # E.g, for Japanese, change into: speech_exceptions = ja_speech_exceptions
    ##########
    speech_exceptions = speechPauses.en_speech_exceptions

## EN
translate en python:
    speech_exceptions = speechPauses.en_speech_exceptions
translate en_uk python:
    speech_exceptions = speechPauses.en_speech_exceptions
translate en_us python:
    speech_exceptions = speechPauses.en_speech_exceptions

## ES
translate es python:
    speech_exceptions = speechPauses.es_speech_exceptions
translate es_es python:
    speech_exceptions = speechPauses.es_speech_exceptions
translate es_mx python:
    speech_exceptions = speechPauses.es_speech_exceptions

## JA
translate ja python:
    speech_exceptions = speechPauses.jp_speech_exceptions

## ID
translate id python:
    speech_exceptions = speechPauses.id_speech_exceptions


###############################################################################################################
################################################# DANGER ZONE #################################################
###############################################################################################################
## Only edit beyond here if you know what you are doing
## But we know that you know, that you know what you are doing... Right?
###############################################################################################################


init 100:

    ## These are the values you override. See example "partOfMyScript" above

    default speechPauses.enabled = None
    default speechPauses.pause_comma_override = None
    default speechPauses.pause_period_override = None


init 100 python in speechPauses:


    ############################################# The Juice ###################################################
    #  This is the main juice. The juicy part of this tool.
    #  Ready? No? Yes? Ok!
    ##################################################


    import re
    from functools import partial
    from store import persistent, config

    # These two are caching and escaping the multiple possibilities for each type.
    # Escaping makes sure the text is not interpreted with a special meaning.
    # E.g. a "?" will mean "optional" but we want it to mean a literal "?".
    # E.g. This turns: [".", "?"]
    # into: "\.|\?"
    comma_separates = '|'.join(re.escape(comma_separate) for comma_separate in speech_comma)
    period_separates = '|'.join(re.escape(period_separate) for period_separate in speech_period)

    # Here I pre-process the exceptions. I want to organize them by text size. This helps the code later.
    exception_sizes = {}
    for speech_exception in speech_exceptions:
        exception_sizes.setdefault(len(speech_exception), []).append(speech_exception)

    # Keeping track of which size is the largest
    exception_sizes_max = max(exception_sizes)

    # This is the main part where the punctuation is found
    # This syntax is regex (you can see more at https://regex101.com/)
    # The task here is straightforward. Find the commas and periods for later processing
    search_pattern = ""
    search_pattern += "\\b"  # This means: There must have been a character before. This ensures if `.` is listed but `...` isn't, it won't match a `...`
    search_pattern += "(?:"  # This creates a group. It's necessary for the `|` that comes a few lines after
    search_pattern +=     "(?P<comma_pause>"  # This is a capture with a name (this goes to match.group("comma_pause"))
    search_pattern +=       comma_separates  # All possibilities for a "comma"
    search_pattern +=     ")"
    search_pattern +=   "|"  # This is an alternate between comma_separates and period_separates. It means I want to capture one of either
    search_pattern +=     "(?P<period_pause>"  # This is a capture with a name (this goes to match.group("period_pause"))
    search_pattern +=       period_separates  # All possibilities for a "period"
    search_pattern +=     ")"
    search_pattern += ")"  # In sum: Succeed when you find either a 'comma' or a 'period' and record which one you got.
    search_pattern += "(?!"  # This is a Look ahead and this must not happen
    search_pattern +=     "$"  # This represents the end of the string. Means I don't want this to success if the text ends right after
    search_pattern +=   "|"
    search_pattern +=     comma_separates  # All possibilities for a "comma" (meaning: I don't want to consider a comma if it's followed by a comma. Just consider the last comma)
    search_pattern +=   "|"
    search_pattern +=     period_separates  # All possibilities for a "period" (meaning: I don't want to consider a period if it's followed by a period. Just consider the last period)
    search_pattern += ")"  # In sum: Overrule previous success if the paragraph ends right there or if there's more punctuation.

    pattern = re.compile(search_pattern)

    ##
    # This is responsible for processing the string
    ##
    def replacer(pause_comma, pause_period, match:re.Match):

        # Figure out which one was caught
        is_comma = match.group("comma_pause") is not None
        is_period = match.group("period_pause") is not None
        text = ""
        pause = 0

        # Keep track of what character was caught. It will be needed later
        if is_comma:
            text = match.group("comma_pause")
            pause = pause_comma  # Knowing it's a comma, pause will be the comma pause time.
        if is_period:
            text = match.group("period_pause")
            pause = pause_period  # Knowing it's a period, pause will be the comma pause time.

        # For simplification later, this gets the characters immediately before the ones caught by the regex above.
        # I need this to compare with the exceptions so I can validate whether this capture is exempt from pausing.
        # I must use `max` to make sure I don't go beyond the beginning of the string when getting this portion.
        initial_slice = match.string[max(0, 4, match.start() - exception_sizes_max + 1):match.start()] + text

        try:
            # Is this matching a dot part of a float number in a tag?
            if initial_slice[-1] == '.':
                # This is not a rigurous test but I'll do like this to simplify the code.
                if initial_slice[-2] == '=':
                    return text

                if initial_slice[-2].isdigit() and initial_slice[-3] == '=':
                    return text
        except IndexError:
            pass


        ##
        # Here is where grouping simplifies. the job
        # I can now test in bulk if any exception applies.
        for exception_size, exceptions in exception_sizes.items():
            test_index = match.start() - exception_size
            ## Here I'm testing the exception as a complete part.
            # E.g. Without this, and with "Mr." as an exception, It would also consider `whateverhereMr.` as an exception too
            if test_index >= 0 and match.string[test_index].isalpha():
                continue

            # Here I'm testing if it's an exception. All exceptions with the same size are tested in one go in that single line
            if initial_slice[exception_size - exception_sizes_max:] in exceptions:
                return text

        # This is the actual work. This adds the pause after the punctuation using cps.
        return (
            text +
            "{cps=" + pause + "}" +
            "\u200B" +  ## \u200B is a space that doesn't take space. AKA zero-width space. It's a real thing: https://en.wikipedia.org/wiki/Zero-width_space
            "{/cps}"
        )


    ##
    # Takes the target time in seconds and turns it into cps
    # The relative version is an estimate but seemed a quite good one as of now
    # Used by add_speech_pauses
    def convert_seconds_to_cps(pause):
        if pause is None:
            return pause

        try:
            if isinstance(pause, str) and pause[0] == '*':
                return '*' + str(1 / float(pause[1:]) / 100)  # Dividing by 100 is KigyoDev's idea and I like it
            else:
                return str(1 / float(pause))
        except ZeroDivisionError:
            return "*1"


    ##
    # Adds cps tags with pause time. This is the entrance function called by Ren'Py to make this work
    ##
    def add_speech_pauses(text_input):
        ## This makes sure I'm not overriding an existing say_menu_text_filter set by something else
        if prev_filter:
            text_input = prev_filter(text_input)

        ## Here I'm just figuring out if this feature is active or not. `enabled` variable has priority

        # do strict check
        if enabled is None:
            if persistent._brunoais__speech_pauses_enabled is not True:
                return text_input

        # do strict check
        if enabled is False:
            return text_input


        ## Keeping the priorities into account, here I do:
        # 1. Figure out if the value was overridden
        # 2. Figure out if the user set a relative or an absolute value
        # 3. Convert whichever correct value decided from seconds to characters per second (cps)

        pause_comma = convert_seconds_to_cps(pause_comma_override)
        if pause_comma is None:
            if persistent._brunoais__speech_pause_comma_relative_enabled:
                pause_comma = convert_seconds_to_cps('*' + str(persistent._brunoais__speech_pause_comma_relative))
            else:
                pause_comma = convert_seconds_to_cps(persistent._brunoais__speech_pause_comma)

        pause_period = convert_seconds_to_cps(pause_period_override)
        if pause_period is None:
            if persistent._brunoais__speech_pause_period_relative_enabled:
                pause_period = convert_seconds_to_cps('*' + str(persistent._brunoais__speech_pause_period_relative))
            else:
                pause_period = convert_seconds_to_cps(persistent._brunoais__speech_pause_period)


        # `partial` allows me to just provide two parameters in advance. So, when sub calls prefilled_replacer, `pause_comma` and `pause_period` are already set
        prefilled_replacer = partial(replacer, pause_comma, pause_period)

        # This is the function responsible for finding what to replace. This is a python stdlib method (see: https://docs.python.org/3.9/library/re.html#re.Pattern.sub).
        return pattern.sub(prefilled_replacer, text_input)


    ## Initialization #############################################################################################
    # If your project already makes use of [config.say_menu_text_filter], this makes sure that your filter is also called in addition to mine.

    prev_filter = config.say_menu_text_filter
    config.say_menu_text_filter = add_speech_pauses


## Licence ####################################################################################################

# original Copyright 2025 KigyoDev
# Copyright 2025 brunoais

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions
# of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Note: Keeping license the same as original author out of respect
