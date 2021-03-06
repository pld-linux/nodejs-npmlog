%define		pkg	npmlog
Summary:	logger for npm
Name:		nodejs-%{pkg}
Version:	0.1.1
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	720d5edefdee24cb3742a44584ef1d29
URL:		https://github.com/isaacs/npmlog
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-ansi < 0.4
Requires:	nodejs-ansi >= 0.3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
logger for npm.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -a package.json log.js $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example.js $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{nodejs_libdir}/%{pkg}
%{_examplesdir}/%{name}-%{version}
