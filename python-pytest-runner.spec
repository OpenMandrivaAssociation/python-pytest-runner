Summary:	Python testsuite framework
Name:		python-pytest-runner
Version:	5.3.1
Release:	2
Group:		Development/Python
License:	MIT
Url:		https://pypi.org/project/pytest-runner/#files
Source0:	https://files.pythonhosted.org/packages/2a/04/c3223812b3427ffa95110c5781eae7fe8bc3e9e1fe4e2328bee17b9e5820/pytest-runner-5.3.1.tar.gz
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
%{py_puresitedir}/ptr.py
