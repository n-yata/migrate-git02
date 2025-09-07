## Git リポジトリの移行検討

一度だけの移行で実施する。過去のリモートリポジトリは利用できなくなる  
全ブランチの情報も移行する。  
git-filter-repo を利用する  
https://raw.githubusercontent.com/newren/git-filter-repo/main/git-filter-repo  
$ pip install git-filter-repo

- 操作コマンド

  ```bash
  # 全ブランチ・全タグを含んだリポジトリをclone
  git clone --mirror https://git-codecommit.ap-northeast-1.amazonaws.com/v1/repos/your-repo
  cd your-repo.git
  # 全ブランチのディレクトリ階層を変更する
  git filter-repo --path lambda/ --to-subdirectory-filter app/lambda
  # 3. 先リモートリポジトリのURLに変更
  git remote set-url origin https://gitlab.com/your-group/your-repo.git
  # 全履歴を先リモートリポジトリに強制push
  git push --mirror --force
  ```
