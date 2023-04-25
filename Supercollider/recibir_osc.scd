OSCFunc({ | args |
	 "OSCFunc received the following values from message '/number':".postln;
	 args[1..].postln;
}, '/number');