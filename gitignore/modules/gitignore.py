import os
import subprocess;

path = os.path.join(os.pardir)
from constants import *
print("import gitignore");

def gitignore(args):
	if args[0] == "init":
		try:
			path_arg = args[1];
			dir_path = os.path.abspath(path_arg);

		except:
			dir_path = os.path.abspath("./");

		gitignore_path = dir_path + "/.gitignore";
		is_gitignore = os.path.isfile(gitignore_path);

		if is_gitignore:
			print("すでに.gitignoreは存在します")
		else:
			f = open(gitignore_path, "w");
			f.write("#");
			f.close();

		return SHELL_STATUS_RUN;

	else:
		gitignore_path = "./.gitignore";
		is_gitignore = os.path.isfile(gitignore_path);

		if not is_gitignore:
			print(".gitignoreが見つかりません")
			return SHELL_STATUS_RUN;

		with open (gitignore_path,"r") as f:
			data = f.readlines();

		none_line_feed_text = data[0].replace(",\n", "").replace("#","");
		li_directory_data = none_line_feed_text.split(",");

		i = 0;
		is_dir = False;
		while True:
			try:
				args[i];
				if args[i] == "-d":
					is_dir = True;
					i += 1;
					args[i];
			except:
				break;


			try:
				for directory in li_directory_data:
					if directory == args[i]:
						print(args[i]+" はすでにgitignoreされています")
						i += 1;

						raise Exception;
			except:
				continue;

			_data = data[0].replace("\n", "") + args[i] + "," + "\n";
			data[0] = _data;

			cmd = "find ./ -name " + args[i];
			result = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).stdout.readlines();

			if is_dir:
				for item in result:
					create_line = item.decode("utf-8").replace("\n","") + "/" + "\n";
					data.append(create_line);
	
				is_dir = False;
			else:
				for item in result:
					data.append(item.decode('utf-8'));
				
			i += 1;
			print(data)

			with open (gitignore_path, "w") as f:
				f.writelines(data);


	return SHELL_STATUS_RUN
