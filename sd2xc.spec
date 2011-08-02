%define name sd2xc
%define version 0.0.4
%define pre RC1
%define release %mkrel 0.%pre.5
%define oname SD2XC

Summary: SD2XC stands for StarDock to Xcursor
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{oname}-%{version}-%pre.perl.bz2
URL: http://www.bwbohh.net/software/SD2XC/index.html
License: MIT
Group: Graphics
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: perl-Magick
Requires: perl-Config-IniFiles
BuildArch: noarch

%description
Converts StarDock CursorXP themes (http://www.wincustomize.com/) to
XCursor themes compatible with XFree86 4.2.99 and higher.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_bindir
bzip2 -cd %SOURCE0 > %buildroot%_bindir/%name


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) %_bindir/%name
