# Anti-Naughtiness Device 2000

I started on this script while I was studying at university, so this is why there are references to classes and school there (not talking about Python classes). I will now proceed to describe what it does and how I personally use it.

The script runs at startup and does not terminate. The intention is not to let me use the Internet between 00:30 and 08:30, and not to let me use the computer at all between 01:30 and 08:30. (I made all these times variable, so feel free to modify them as you wish, though I still need to fix the situation where the times cross days.) If any web browsers are open between 00:30 and 08:30, they are forcefully terminated. Furthermore, if the computer is turned on between 01:30 and 08:30, it is forcefully shut down.

The program also gives warnings if these times are approaching. If you have browser windows open 10 minutes before the forbidden time, the program warns you using a pop-up notification and a robot voice. (This is the only way I could find that would be guaranteed to catch my attention.) Also, 10 minutes before the shutdown time, it will warn you, repeatedly and nonstop, that your computer is about to shut down. If you turn on your computer in the middle of the shutdown time, it will warn you for 5 minutes instead.

For the version I released to the public, which is the version here, I have removed the robot voice but may reimplement it later. Only a pop-up notification will be displayed.

## Important note
If you wish to have this script shut down your computer, you need to add the relevant permissions to your sudoers file.

regulators.py is the file that is to be run at startup.

## Things I still need to do
- [ ] Add Windows support
- [ ] Make the application more difficult to terminate
