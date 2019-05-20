# bcf2000-py

Python script for controlling BCF2000 control surface

This is a script for using the Behringer BCF2000 or BCR2000 control surface in non-musical applications.

The BCx2000 control surfaces are sold as MIDI controllers, but they can be useful in non-MIDI context to control (and readout) other realtime programs.

Most of the information available about these controllers involve a lot of detail about the MIDI specification.

Here is a script that ignores all that, and just configures the faders as 14-bit inputs and motorized outputs.

The configuration is loaded into the temporary preset, so it doesn't interfere with MIDI uses of the control surface.

The script uses Python 2 on Linux.  (It just interacts with a character device to send and receive MIDI, so I expect it can work on other platforms.)

As written, it is an example of configuring faders and encoders over SysEx, and an example that ties fader 1 position to fader 2 and vice-versa.
