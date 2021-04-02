function! SomeCheck(path)
    if file_readable(a:path)
        return 1
    endif
    return 0
endfunction

function! CheckTestExist(fullpath, problem_name)
    let array = split(a:fullpath, "/")
    " /Users/treo/Workspase/atcoder/problems/abc150_a.py
    let a_len = len(array)
    let tmp = remove(array, -2,-1) " 'remove()' return removed elements 微妙
    let test_dir_path = join(add(array, "test/".a:problem_name),"/")

    return test_dir_path
endfunction

function! CheckInstalledOj() abort
    if ! exists("g:oj_command")
        let g:oj_command = 'oj'
    endif

    " if you don't have oj command, you will install that by pip3
    if ! executable(g:oj_command)
        try
            execute "!pip3 install online-judge-tools"
        catch
            echo("we use \"pip3\". \n Please install.")
        endtry
    endif
endfunction

function! GetFileName(path) abort
    let array = split(a:path,"/")
    let a_len = len(array)

    return get(array,a_len - 1)
endfunction

function! ACVtest() abort
    let fullpath = expand("%:p") " /Users/treo/Workspase/atcoder/problems/abc150_a.py
    let problem_name = GetFileName(expand("%<")) " abc150_a
    let contest_name=split(problem_name,"_")[0] " abc150

    let test_dir = CheckTestExist(fullpath, problem_name)

    if !isdirectory(test_dir)
        :silent execute "!oj dl -d " . test_dir . " https://atcoder.jp/contests/" . contest_name . "/tasks/" . problem_name
    endif

    execute "!oj test -c " . "\"python " . fullpath . "\" -d " . test_dir
endfunction

" main
execute CheckInstalledOj()
execute ACVtest()
