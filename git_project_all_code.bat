@echo off

set work_path=E:\Code\git_code\1_ONLY_PULL\project_xxxx
cd /d %work_path%
call :pull_git_code project-liquidator git@github.com:project/project-liquidator.git
call :pull_git_code project-configs git@github.com:project/project-configs.git
call :pull_git_code project-dapp git@github.com:project/project-dapp.git
call :pull_git_code project-core git@github.com:project/project-core.git
cd /d %work_path%
ls
goto :eof


REM pull_git_code
:pull_git_code
echo pull_git_code
echo %1
echo %2
cd /d %work_path%
echo "%work_path%\%1"

IF EXIST "%work_path%\%1" (
    echo %1 exists!
    echo pull new code
    cd %1
    git pull
    IF %errorlevel% equ 0 (
        echo git code ok
    ) ELSE (
        git fetch --all
        git reset --hard origin/master
        git pull
    ) 
) ELSE (
    echo %1 does not exist.
    echo "git clone code"
    git clone %2
)
goto :eof


