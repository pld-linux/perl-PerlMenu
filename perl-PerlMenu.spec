%include	/usr/lib/rpm/macros.perl
%define		pdir	perlmenu
Summary:	PerlMenu - Perl library module for curses-based menus & data-entry templates
Summary(pl.UTF-8):	PerlMenu - moduł Perla z menu opartymi na curses i szablonami dla danych
Name:		perl-PerlMenu
Version:	4.0
Release:	2
License:	LGPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SK/SKUNZ/%{pdir}.v%{version}.tar.gz
# Source0-md5:	b931859ed581970f3fb05420316b39d3
Patch0:		%{name}-tput.patch
URL:		http://www.cc.iastate.edu/perlmenu/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PerlMenu - Perl library module for curses-based menus & data-entry
templates.

%description -l pl.UTF-8
PerlMenu - moduł biblioteki Perla z menu opartymi na curses oraz
szablonami formularzy do wpisywania danych.

%prep
%setup  -q -n %{pdir}.v%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{perl_vendorlib},%{_examplesdir}/%{name}-%{version}}

install -m644 perlmenu.pm menuutil.pl $RPM_BUILD_ROOT%{perl_vendorlib}
for item in demo* ez* paint* template* ; do
	sed 's=#!/usr/local/bin/perl5=!/usr/bin/perl=' <$item \
	>$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$item
done
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ MENUUTIL_DOC MENU_DOC README RELEASE_NOTES TO_DO
%{perl_vendorlib}/*
%{_examplesdir}/%{name}-%{version}
