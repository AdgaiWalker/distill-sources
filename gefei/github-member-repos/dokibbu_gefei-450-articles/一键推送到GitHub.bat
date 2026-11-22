@echo off
chcp 65001 >nul
title 哥飞文库 - 推送到 GitHub

echo ===================================================
echo   正在准备推送到 GitHub 仓库...
echo ===================================================
echo.

cd /d "%~dp0"

echo 当前目录: %CD%
echo 正在执行: git push -u origin main
echo.

git push -u origin main

echo.
if %ERRORLEVEL% equ 0 (
    echo ===================================================
    echo   [成功] 代码已成功推送到 GitHub!
    echo ===================================================
) else (
    echo ===================================================
    echo   [提示] 推送遇到问题，请检查:
    echo   1. GitHub 上是否已创建仓库 (gefei-450-articles)
    echo   2. 是否弹出了浏览器授权窗口并点击允许
    echo ===================================================
)

echo.
pause
