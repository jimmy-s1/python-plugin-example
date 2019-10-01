import importlib.util
import os

PLUGINS = []

def runPlugins():
	for plugin in PLUGINS:
		plugin.run()


def loadPlugins(dir):
	for file in os.listdir(dir):
		# only load .py files
		if(file.endswith(".py")==False):
			break
			
		# load plugin
		spec = importlib.util.spec_from_file_location(file, dir+file)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)

		# add Plugin class to list
		PLUGINS.append(module.Plugin)

		print("Plugin loaded:", module.Plugin.getPluginName(), "from", file)
	


if(__name__=="__main__"):
	loadPlugins("plugins/")
	runPlugins()
