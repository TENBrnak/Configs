set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'

Plugin 'codota/tabnine-vim'

call vundle#end()
filetype plugin indent on

set number
set autoindent
set textwidth=80
set encoding=utf-8
syntax on
inoremap jj <Esc>
