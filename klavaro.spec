Summary:	Touch typing tutor program
Summary(pl):	Program do nauki pisania bezwzrokowego na klawiaturze
Name:		klavaro
Version:	0.9.7
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/klavaro/%{name}-%{version}.tar.gz
URL:		http://klavaro.sourceforge.net/en/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.6.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Klavaro is a program that teachs you to touch type and/or helps you to
improve your skills with the keyboard.

%description -l pl
Klavaro jest programem do nauki i/lub poprawy umiejêtno¶ci pisania
bezwzrokowego na klawiaturze.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f klavaro.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
