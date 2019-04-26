class Assistant:

    def greet(self):
        print("================ Remote Environment Helper ================\n")
        self.speak("Hello there!")

    def speak(self, data):
        print("Your personal assistant> %s" % data)

    def list_options(self, options):
        self.speak("Available options:")
        for key, value in sorted(options):
            print("* %s" % key)
        print("")

    def say_goodbye(self):
        self.speak("You could at least say thanks...")
