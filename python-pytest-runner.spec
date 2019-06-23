Summary:	Python testsuite framework
Name:		python-pytest-runner
Version:	5.1
Release:	2
Group:		Development/Python
License:	MIT
Url:		https://pypi.org/project/pytest-runner/#files
Source0:	https://files.pythonhosted.org/packages/d9/6d/4b41a74b31720e25abd4799be72d54811da4b4d0233e38b75864dcc1f7ad/pytest-runner-5.1.tar.gz
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
