# NOTE: obsoleted in favour of synce-core.spec
Summary:	SynCE DCCM - daemon to communicate with Pocket PC device
Summary(pl.UTF-8):	SynCE DCCM - demon do komunikacji z urządzeniem Pocket PC
Name:		synce-dccm
Version:	0.9.1
Release:	1
License:	MIT
Group:		Applications/Networking
Source0: 	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	8818b71133049fe9c739166225aebe0c
URL:		http://www.synce.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.4
BuildRequires:	libtool
BuildRequires:	synce-libsynce-devel >= 0.9.0
# for play
Requires:	sox
Requires:	synce-libsynce >= 0.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DCCM is a daemon required to be able to communicate with a handheld
device. It's part of SynCE project.

%description -l pl.UTF-8
DCCM to demon potrzebny do komunikowania się z urządzeniem Pocket PC.
Jest on częścią projektu SynCE.

%prep
%setup -q

%build
%{__libtoolize}
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README TODO
%attr(755,root,root) %{_bindir}/dccm
%attr(755,root,root) %{_bindir}/synce-sound
%{_mandir}/man1/dccm.1*
%{_mandir}/man1/synce-sound.1*
