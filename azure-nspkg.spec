#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-nspkg
Version  : 3.0.2
Release  : 9
URL      : https://files.pythonhosted.org/packages/39/31/b24f494eca22e0389ac2e81b1b734453f187b69c95f039aa202f6f798b84/azure-nspkg-3.0.2.zip
Source0  : https://files.pythonhosted.org/packages/39/31/b24f494eca22e0389ac2e81b1b734453f187b69c95f039aa202f6f798b84/azure-nspkg-3.0.2.zip
Summary  : Microsoft Azure Namespace Package [Internal]
Group    : Development/Tools
License  : MIT
Requires: azure-nspkg-python = %{version}-%{release}
Requires: azure-nspkg-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
==============================
        
        This is the Microsoft Azure namespace package.
        
        This package is not intended to be installed directly by the end user.

%package python
Summary: python components for the azure-nspkg package.
Group: Default
Requires: azure-nspkg-python3 = %{version}-%{release}

%description python
python components for the azure-nspkg package.


%package python3
Summary: python3 components for the azure-nspkg package.
Group: Default
Requires: python3-core
Provides: pypi(azure_nspkg)

%description python3
python3 components for the azure-nspkg package.


%prep
%setup -q -n azure-nspkg-3.0.2
cd %{_builddir}/azure-nspkg-3.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583531448
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
