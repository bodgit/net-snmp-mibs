Name: net-snmp-mibs
Version: 1.0
Release: 1
URL: https://github.com/bodgit/net-snmp-mibs
Group: System Environment/Daemons
Distribution: Red Hat Linux
Packager: Matt Dainty <matt@bodgit-n-scarper.com>
License: BSD
Summary: Extra MIB files for NET-SNMP.

Prefix: %{_prefix}

Buildroot: %{_tmppath}/%{name}-%{version}-root
Buildarch: noarch
Requires: net-snmp

Source0: http://www.simpleweb.org/ietf/mibs/modules/IETF/txt/PerfHist-TC-MIB
Source1: http://www.simpleweb.org/ietf/mibs/modules/IETF/txt/ADSL-TC-MIB
Source2: http://www.simpleweb.org/ietf/mibs/modules/IETF/txt/ADSL-LINE-MIB
Source3: http://www.simpleweb.org/ietf/mibs/modules/IETF/txt/ADSL-LINE-EXT-MIB

%description
Extra MIB files for NET-SNMP.

%prep
%setup -c -T
%{__install} %{SOURCE0} .
%{__install} %{SOURCE1} .
%{__install} %{SOURCE2} .
%{__install} %{SOURCE3} .

%build
for i in *-MIB ; do
	%{__mv} ${i} ${i}.txt
done

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_datadir}/snmp/mibs
%{__install} *-MIB.txt $RPM_BUILD_ROOT%{_datadir}/snmp/mibs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root)
%{_datadir}/snmp/mibs/*

%changelog
* Sat Feb 26 2011 Matt Dainty <matt@bodgit-n-scarper.com> 1.0-1
- Initial version containing ADSL MIB files.
