#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vim
import os
import os.path
import fnmatch
import subprocess
from leaderf.utils import *
from leaderf.explorer import *
from leaderf.manager import *

#*****************************************************
# DiffusateExplorer
#*****************************************************
class DiffusateExplorer(Explorer):
    def __init__(self):
        pass

    def getContent(self, *args, **kwargs):
        """
        Get display content
        """
        pathroot = ''
        docfilter = ''
        if kwargs.get("arguments", {}).get("path"):
            pathroot = kwargs.get("arguments", {}).get("path")[0]
            if not pathroot:
                return None

        if kwargs.get("arguments", {}).get("filter"):
            docfilter = kwargs.get("arguments", {}).get("filter")[0]
            if not docfilter:
                return None

        return self.__validDocsList(pathroot, docfilter)


    def getStlCategory(self):
        return "Diffusate"

    def getStlCurDir(self):
        return escQuote(lfEncode(os.getcwd()))

    def __validDocsList(self, pathroot, docfilter):
        pathlist = pathroot.split(';')
        filter(None, pathlist)

        docfilelist = []
        filterlist = docfilter.split(';')
        dirignore = filterlist[0].split(',')
        fileinclude = filterlist[1].split(',')
        for path in pathlist:
            self.__getFiles(docfilelist, path, dirignore, fileinclude)

        return docfilelist

    def __getFiles(self, docfilelist, path, dirignore, fileinclude):
        for dir_path, dirs, files in os.walk(path, followlinks = False):
            dirs[:] = [i for i in dirs if True not in (fnmatch.fnmatch(i,j) for j in dirignore)]
            for name in files:
                if True in (fnmatch.fnmatch(name, j) for j in fileinclude):
                    docfilelist.append(os.path.join(dir_path,name))

#*****************************************************
# DiffusateExplManager
#*****************************************************
class DiffusateExplManager(Manager):
    def __init__(self):
        super(DiffusateExplManager, self).__init__()
        self._match_ids = []
        self._ftype = ''

    def _getExplClass(self):
        return DiffusateExplorer

    def _defineMaps(self):
        lfCmd("call leaderf#diffusatefile#Maps()")

    def _acceptSelection(self, *args, **kwargs):
        """
        If select one, how process it?
        """
        if len(args) == 0:
            return
        filename = args[0]

        execmap = lfEval("g:leaderf_diffusate_exec_map")

        # open file or edit file
        #  print(filename)
        if fnmatch.fnmatch(filename, '*.md'):
            lfCmd("hide edit %s" % escSpecial(filename))
        elif fnmatch.fnmatch(filename, '*.txt'):
            lfCmd("hide edit %s" % escSpecial(filename))
        elif fnmatch.fnmatch(filename, '*.pdf'):
            #  execargs = "%s %s" % (execmap['pdf'], filename)
            #  os.system(execargs)
            #  subprocess.Popen([execmap['pdf'], filename])
            execcmd = "call system('%s %s &')"%(execmap['pdf'], filename)
            lfCmd(execcmd)
        elif fnmatch.fnmatch(filename, '*.doc'):
            execcmd = "call system('%s %s &')"%(execmap['doc'], filename)
            lfCmd(execcmd)
        elif fnmatch.fnmatch(filename, '*.chm'):
            execcmd = "call system('%s %s &')"%(execmap['chm'], filename)
            lfCmd(execcmd)


    def _getDigest(self, line, mode):
        """
        specify what part in the line to be processed and highlighted
        Args:
            mode: 0, 1, 2, return the whole line
        """
        if not line:
            return ''
        return line[1:]

    def _getDigestStartPos(self, line, mode):
        """
        return the start position of the digest returned by _getDigest()
        Args:
            mode: 0, 1, 2, return 1
        """
        return 1

    def _createHelp(self):
        help = []
        help.append('" <CR>/<double-click>/o : execute command under cursor')
        help.append('" i : switch to input mode')
        help.append('" q : quit')
        help.append('" <F1> : toggle this help')
        help.append('" ---------------------------------------------------------')
        return help

    def _afterEnter(self):
        super(DiffusateExplManager, self)._afterEnter()

    def _beforeExit(self):
        super(DiffusateExplManager, self)._beforeExit()
        for i in self._match_ids:
            lfCmd("silent! call matchdelete(%d)" % i)
        self._match_ids = []

    def startExplorer(self, win_pos, *args, **kwargs):
        if kwargs.get("arguments", {}).get("path"):
            super(DiffusateExplManager, self).startExplorer(win_pos, *args, **kwargs)
            return

        return


#*****************************************************
# diffusateExplManager is a singleton
#*****************************************************
diffusateExplManager = DiffusateExplManager()
__all__ = ['diffusateExplManager']
