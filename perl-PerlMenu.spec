%include	/usr/lib/rpm/macros.perl
%define	pdir	perlmenu
Summary:	PerlMenu - Perl library module for curses-based menus & data-entry templates
Summary(pl):	PerlMenu - modu³ Perla z menu opartymi na curses i szablonami dla danych
Name:		perl-PerlMenu
Version:	4.0
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SK/SKUNZ/%{pdir}.v%{version}.tar.gz
Patch0:		%{name}-tput.patch
URL:		http://www.cc.iastate.edu/perlmenu/
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PerlMenu - Perl library module for curses-based menus & data-entry
templates.

%description -l pl
PerlMenu - modu³ biblioteki Perla z menu opartymi na curses oraz
szablonami formularzy do wpisywania danych.

%prep
%setup  -q -n %{pdir}.v%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{perl_sitelib},%{_examplesdir}/%{name}-%{version}}

install -m644 perlmenu.pm menuutil.pl $RPM_BUILD_ROOT%{perl_sitelib}
for item in demo* ez* paint* template* ; do 
	sed 's=#!/usr/local/bin/perl5=!/usr/bin/perl=' <$item \
	>$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$item
done
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ MENUUTIL_DOC MENU_DOC README RELEASE_NOTES TO_DO
%{perl_sitelib}/*
%{_examplesdir}/%{name}-%{version}
