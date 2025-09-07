# 全ブランチを取得して処理する
$branches = git for-each-ref --format="%(refname:short)" refs/heads/

foreach ($branch in $branches) {
    Write-Host "Processing branch: $branch"

    # ブランチをチェックアウト
    git checkout $branch

    # dir ディレクトリがある場合だけ処理
    if (Test-Path "dir") {
        if (!(Test-Path "app")) {
            New-Item -ItemType Directory -Path "app" | Out-Null
        }

        # dir を app/dir に移動
        git mv dir app/dir
        git commit -m "Move dir/ to app/dir/"
    } else {
        Write-Host "No 'dir' directory found in branch: $branch"
    }
}
