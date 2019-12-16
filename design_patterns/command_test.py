class Command:
	def execute(self):
		pass

class Copy(Command):
	def execute(self):
		print("Copying ...")

class Paste(Command):
	def execute(self):
		print("Saving ...")

class Save(Command):
	def execute(self):
		print("Saveing ...")

class Macro:
	def __init__(self):
		self._commands = []

	def add(self, command):
		self._commands.append(command)

	def run(self):
		for o in self._commands:
			o.execute()

def main():
	marco = Macro()
	marco.add(Copy())
	marco.add(Paste())
	marco.add(Save())
	marco.run()

if __name__ == "__main__":
	main()
