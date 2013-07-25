# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:		python-xrcctrl
Version:	0.2
Release:	1%{?dist}
Summary:    XRC base classes for building wx widgets controls that extend controls defined in XRC resources.	

Group:		Development/Languages
License:	GPL
URL:		http://www.ubixum.com
Source0:	%{name}-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch
# BuildRequires: 
# Requires: 

%description
%{summary}

%prep
%setup -q


%build
# Remove CFLAGS=... for noarch packages (unneeded)
# CFLAGS="$RPM_OPT_FLAGS" \
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
# For noarch packages: sitelib
#%{python_sitelib}/*
# For arch-specific packages: sitearch
%{python_sitelib}/*


%changelog

