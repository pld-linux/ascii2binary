#
Summary:	Two complementary programs that convert between textual and binary representations of numbers
Summary(pl):	Dwa uzupe�niaj�ce si� programy zamieniaj�ce tekstow� i binarn� reprezentacj� liczb
Name:		ascii2binary
Version:	2.12
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.billposer.org/Software/Downloads/%{name}-%{version}.tgz
# Source0-md5:	71a75ab5b77ae047b257baa180c07cf2
URL:		http://billposer.org/Software/a2b.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Ascii2Binary project consists of two complementary programs that
convert between textual and binary representations of numbers. In both
programs, the type and size/precision of the input or output is
selected using command line flags.

%description -l pl
Ascii2Binary zawiera dwa uzupe�niaj�ce si� programy zamieniaj�ce
tekstow� oraz binarn� reprezentacj� liczb. W obu programach typ oraz
rozmiar i precyzja danych jest wybierania na podstawie flag linii
polece�.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS INSTALL NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*