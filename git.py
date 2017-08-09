from subprocess import call

call(["git", "add", "./"])
call(["git", "commit", "-m", "\"Automatic commit\""])
call(["git", "push", "origin", "master"])
