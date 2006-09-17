Summary:	Touch typing tutor program
Summary(pl):	Program do nauki pisania bezwzrokowego na klawiaturze
Name:		klavaro
Version:	0.9.9
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/klavaro/%{name}-%{version}.tar.gz
# Source0-md5:	2f8b79dbe3e94dcca8646576afeb2325
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://klavaro.sourceforge.net/en/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.6.2
BuildRequires:	pkgconfig
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
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

mv $RPM_BUILD_ROOT%{_datadir}/locale/{cs_CZ,cs}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{de_DE,de}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{eo_EO,eo}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{fr_FR,fr}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{hu_HU,hu}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{sv_SE,sv}
%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
