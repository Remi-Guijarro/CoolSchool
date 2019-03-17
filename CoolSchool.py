from session import run
import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
        


if __name__ == "__main__":
	install("colorama")
	run()