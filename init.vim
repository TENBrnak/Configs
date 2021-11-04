call plug#begin()

Plug 'codota/tabnine-vim'
Plug 'Chiel92/vim-autoformat'
Plug 'numirias/semshi', {'do': ':UpdateRemotePlugins'}
Plug 'dense-analysis/ale'

Plug 'jiangmiao/auto-pairs'

Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

call plug#end()

inoremap jj <Esc>
set number
set encoding=utf-8
filetype plugin indent on
syntax on
