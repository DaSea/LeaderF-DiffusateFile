"=============================================================================
" FILE: diffusatefile.vim
" AUTHOR: DaSea
"=============================================================================
if !has('python') && !has('python3')
    finish
endif

if exists('g:loaded_diffusatefile')
    finish
endif
let g:loaded_diffusatefile= 1

let s:save_cpo = &cpo
set cpo&vim

" Variables{{{
if !exists('g:leaderf_diffusate_doc_root')
    " many path is seperate with ';'
    " let path="/path1;path2/"
    let g:leaderf_diffusate_doc_root = ""
endif

" filter: pdf, doc, chm
if !exists('g:leaderf_diffusate_doc_filter')
    " filter is seperate with ';'
    " dir: ignore dir name; file: need to browse:
    let g:leaderf_diffusate_doc_filter="docsets;*.doc,*.pdf,*.txt,*.chm,*.md"
endif

if !exists('g:leaderf_diffusate_notes_root')
    " let path="/path1;path2/"
    let g:leaderf_diffusate_notes_root = ""
endif
if !exists('g:leaderf_diffusate_notes_filter')
    " dir: ignore dir name; file: need to browse:
    let g:leaderf_diffusate_notes_filter="png,about,categories,tags;*.md"
endif

if !exists('g:leaderf_diffusate_exec_map')
    if(has("win32") || has("win64") || has("win95") || has("win16"))
        let g:leaderf_diffusate_exec_map = {
                    \ 'pdf': 'foxit.exe',
                    \ 'doc': ''
                    \}
    else
        let g:leaderf_diffusate_exec_map = {
                    \ 'pdf': 'qpdfview --unique',
                    \ 'doc': 'wps',
                    \ 'chm': 'kchmviewer'
                    \}
    endif
endif
"}}}

" commands{{{
command! -bar -nargs=0 LeaderfDoc call leaderf#diffusatefile#startExpl(g:Lf_WindowPosition, g:leaderf_diffusate_doc_root, g:leaderf_diffusate_doc_filter)
command! -bar -nargs=0 LeaderfNote call leaderf#diffusatefile#startExpl(g:Lf_WindowPosition, g:leaderf_diffusate_notes_root, g:leaderf_diffusate_notes_filter)
"}}}

" Initial {{{
" call g:LfRegisterSelf("LeaderfDoc", "List your document")
" }}}

" vim: foldmethod=marker

