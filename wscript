import Options
from os import symlink, unlink
from os.path import exists 

srcdir = '.'
blddir = 'build'

def set_options(opt):
    opt.tool_options('compiler_cc')

def configure(conf):
    conf.check_tool('compiler_cc')

def build(bld):
    obj = bld.new_task_gen('cc', 'shlib')
    obj.target = 'hello'
    obj.source = 'hello.c'

def shutdown():
    if Options.commands['clean']:
          if exists('libhello.so'):
              unlink('libhello.so')
    else:
        if exists('build/Release/libhello.so') and not exists('libhello.so'):
            symlink('build/Release/libhello.so', 'libhello.so')
