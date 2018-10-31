Summary:	Python testsuite framework
Name:		python-pytest-runner
Version:	4.2
Release:	2
Group:		Development/Python
License:	MIT
Url:		https://pypi.org/project/pytest-runner/#files
Source0:	https://files.pythonhosted.org/packages/9e/b7/fe6e8f87f9a756fd06722216f1b6698ccba4d269eac6329d9f0c441d0f93/pytest-runner-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python-setuptools_scm
BuildArch:	noarch

%description
Python testsuite framework

%files
%{py_puresitedir}/pytest_runner*
%{py_puresitedir}/ptr.py
%{py_puresitedir}/__pycache__/*

%prep
%autosetup -p1 -n pytest-runner-%{version}

%build
python setup.py build

%install
python setup.py install --root %{buildroot}
