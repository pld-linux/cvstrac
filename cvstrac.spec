Summary:	A Web-Based Bug And Patch-Set Tracking System For CVS, Subversion and GIT
Name:		cvstrac
Version:	2.0.1
Release:	0.1
License:	GPL
Group:		Applications/WWW
Source0:	http://www.cvstrac.org/%{name}-%{version}.tar.gz
# Source0-md5:	684bcb739eb5a6e1932fb8797ffe6a91
URL:		http://www.cvstrac.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%{_prefix}/share/%{name}
%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}

%description
A Web-Based Bug And Patch-Set Tracking System For CVS, Subversion and
GIT

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
