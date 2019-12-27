1. Generate an ssh-key with email

```
ssh-keygen -t rsa -C "email@work_mail.com" -f "id_rsa_work_user1"
```

2. 
- Go to github.com/settings. 
- Select `SSH and GPG keys`. 
- Click `New SSH key`
- Add key
3. Ensure ssh-agent is running using the command 
```
eval "$(ssh-agent -s)"
```
4. Add the keys to the ssh-agent like so:
```
ssh-add ~/.ssh/id_rsa
ssh-add ~/.ssh/id_rsa_work_user1
```
5. Create an `ssh-config` file - 
```
cd ~/.ssh/
$ touch config           // Creates the file if not exists
$ code config            // Opens the file in VS code, use any editor
```
6. configure like this - 
```
# Personal account, - the default config
Host github.com
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa
   
# Work account-1
Host github.com-work_user1    
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa_work_user1
```

7. Open `.gitconfig` file and do like this-
```
[user]
	name = Arnab Roy
	email = personal@gmail.com

[includeIf "gitdir:~/my\ world"]
	path = "~/my world/.gitconfig"

[includeIf "gitdir:~/my\ world/work"]
	path = "~/my world/work/.gitconfig"
```

8. In other directories create separate gitconfig files with mail and name - 
```
[user]
	name = Arnab Roy
	email = work@mail.com
```

9. Now to clone repository - 
```
git clone git@github.com-<work_user1>:<work_username>/repo_name.git
```
<work_user1> would be like what you put in the `ssh-config`