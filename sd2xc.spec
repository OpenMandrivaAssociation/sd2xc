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
URL: https://www.bwbohh.net/software/SD2XC/index.html
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


%changelog
* Tue Aug 02 2011 Götz Waschk <waschk@mandriva.org> 0.0.4-0.RC1.5mdv2012.0
+ Revision: 692732
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.0.4-0.RC1.4mdv2011.0
+ Revision: 140782
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 01 2007 Götz Waschk <waschk@mandriva.org> 0.0.4-0.RC1.4mdv2008.0
+ Revision: 57446
- Import sd2xc



* Mon Jul 31 2006 G�tz Waschk <waschk@mandriva.org> 0.0.4-0.RC1.4mdv2007.0
- Rebuild

* Tue Mar 14 2006 G�tz Waschk <waschk@mandriva.org> 0.0.4-0.RC1.3mdk
- fix URL

* Sun Mar 13 2005 Götz Waschk <waschk@linux-mandrake.com> 0.0.4-0.RC1.2mdk
- rebuild

* Fri Feb 27 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.0.4-0.RC1.1mdk
- drop prefix
- newer version

* Mon Mar  3 2003 G�tz Waschk <waschk@linux-mandrake.com> 0.0.3-1mdk
- initial package
