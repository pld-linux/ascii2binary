Summary:	Convert between textual and binary representations of numbers
Summary(pl):	Zamiana miêdzy tekstow± a binarn± reprezentacj± liczb
Name:		ascii2binary
Version:	2.13
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.billposer.org/Software/Downloads/%{name}-%{version}.tar.gz
# Source0-md5:	25682a506a21bdf12f879b3425adc545
URL:		http://billposer.org/Software/a2b.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Ascii2Binary project consists of two complementary programs that
convert between textual and binary representations of numbers. In both
programs, the type and size/precision of the input or output is
selected using command line flags.

%description -l pl
Ascii2Binary zawiera dwa uzupe³niaj±ce siê programy zamieniaj±ce
liczby miêdzy ich tekstow± a binarn± reprezentacj±. W obu programach
typ oraz rozmiar i precyzja danych jest wybierania na podstawie flag
linii poleceñ.

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
