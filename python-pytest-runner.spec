Summary:	Python testsuite framework
Name:		python-pytest-runner
Version:	6.0.1
Release:	1
Group:		Development/Python
License:	MIT
Url:		https://pypi.org/project/pytest-runner/#files
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-runner/pytest-runner-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python-setuptools_scm
BuildArch:	noarch

%description
Python testsuite framework.

%prep
%autosetup -p1 -n pytest-runner-%{version}

%build
%py_build

%install
%py_install

%files
%{py_puresitedir}/pytest_runner*
%{py_puresitedir}/ptr
