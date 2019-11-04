Summary:	Python testsuite framework
Name:		python-pytest-runner
Version:	5.2
Release:	1
Group:		Development/Python
License:	MIT
Url:		https://pypi.org/project/pytest-runner/#files
Source0:	https://files.pythonhosted.org/packages/5b/82/1462f86e6c3600f2471d5f552fcc31e39f17717023df4bab712b4a9db1b3/pytest-runner-5.2.tar.gz
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
