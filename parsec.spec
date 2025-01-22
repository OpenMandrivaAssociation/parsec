%undefine _debugsource_packages

%define exename %{name}d

Summary: Simple, low-latency desktop and game streaming
Name:    parsec
Version: 150_95
Release: 1
License: Proprietary
Group:   Applications/Internet
Url:     https://parsec.app
# Extracted and repackaged from Debian package available at:
# https://builds.parsec.app/package/parsec-linux.deb
Source0: parsec-150_95.tar.zst

ExclusiveArch: %{x86_64}

%description
Remotely connect to a gaming PC for a low latency remote computing experience.

%prep
%autosetup

%install
cp -ar * %{buildroot}/

%files
%{_bindir}/%{exename}
%{_datadir}/applications/
%{_datadir}/%{name}/
%{_iconsdir}/hicolor/*/apps/%{exename}.*
