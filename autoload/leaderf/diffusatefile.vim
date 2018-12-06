" ============================================================================
" File:        diffusatefile.vim
" Description:
" Note:
" License:     Apache License, Version 2.0
" ============================================================================

if leaderf#versionCheck() == 0
    finish
endif

exec g:Lf_py "import vim, sys, os.path"
exec g:Lf_py "cwd = vim.eval('expand(\"<sfile>:p:h\")')"
exec g:Lf_py "sys.path.insert(0, os.path.join(cwd, 'python'))"
exec g:Lf_py "from diffusateExpl import *"

function! leaderf#diffusatefile#Maps()
    nmapclear <buffer>
    nnoremap <buffer> <silent> <CR>   :exec g:Lf_py "diffusateExplManager.accept()"<CR>
    nnoremap <buffer> <silent> q      :exec g:Lf_py "diffusateExplManager.quit()"<CR>
    nnoremap <buffer> <silent> i      :exec g:Lf_py "diffusateExplManager.input()"<CR>
    nnoremap <buffer> <silent> <F1>   :exec g:Lf_py "diffusateExplManager.toggleHelp()"<CR>
endfunction

" function! leaderf#diff#startExpl(win_pos)
    " if 0==len(g:leaderf_docs_root)
        " return
    " endif

    " call leaderf#LfPy("docsExplManager.startExplorer('".a:win_pos."', arguments={'path': ['".g:leaderf_docs_root."'], 'filter':['". g:leaderf_docs_filter."']})")
" endfunction

function! leaderf#diffusatefile#startExpl(win_pos, ...)
    if a:0 == 0
        return
    endif

    let dir = fnamemodify(a:1.'/',":h:gs?\\?/?")
    let filter = a:2
    " echo dir | echo filter
    call leaderf#LfPy("diffusateExplManager.startExplorer('".a:win_pos."', arguments={'path': ['".dir."'], 'filter':['". filter."']})")
endfunction
