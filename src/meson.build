pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'gtksystemd')
gnome = import('gnome')

gnome.compile_resources('gtksystemd',
  'gtksystemd.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')
message('Looking for dependencies')
dependency('libhandy-1', version: '>= 0.90.0')

python3_required_modules = ['numpy']

python_bin = python.find_installation('python3')
if not python_bin.found()
    error('No valid python3 binary found')
else
    message('Found python3 binary')
endif

foreach p : python3_required_modules
    # Source: https://docs.python.org/3/library/importlib.html#checking-if-a-module-can-be-imported
    script = 'import importlib.util; import sys; exit(1) if importlib.util.find_spec(\''+ p +'\') is None else exit(0)'
    if run_command(python_bin, '-c', script).returncode() != 0
        error('Required Python3 module \'' + p + '\' not found')
    endif
endforeach

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'gtksystemd.in',
  output: 'gtksystemd',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

gtksystemd_sources = [
  '__init__.py',
  'main.py',
  'window.py',
]

install_data(gtksystemd_sources, install_dir: moduledir)
