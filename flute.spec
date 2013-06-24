%define with_gcj 0

Name: flute
Version: 1.3.0
Release: %mkrel 3
Summary: Java CSS parser using SAC
# The entire source code is W3C except ParseException.java which is LGPLv2+
License: W3C and LGPLv2+
Group:   System/Libraries
Source0: http://downloads.sourceforge.net/jfreereport/%{name}-%{version}-OOo31.zip
URL: http://www.w3.org/Style/CSS/SAC/
BuildRequires: ant, java-devel >= 0:1.6.0, jpackage-utils, sac, java-rpmbuild
Requires: java >= 0:1.6.0 , jpackage-utils, sac
%if %{with_gcj}
BuildRequires: java-gcj-compat-devel >= 1.0.31
Requires(post): java-gcj-compat >= 1.0.31
Requires(postun): java-gcj-compat >= 1.0.31
%else
BuildArch: noarch
%endif

%description
A Cascading Style Sheets parser using the Simple API for CSS, for Java.

%package javadoc
Group: Documentation
Summary: Javadoc for %{name}
%if %{with_gcj}
BuildArch: noarch
%endif

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib sac

%build
ant jar javadoc

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%if %{with_gcj}
%{_bindir}/aot-compile-rpm
%endif

%if %{with_gcj}
%post
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{with_gcj}
%postun
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%defattr(0644,root,root,0755)
%doc COPYRIGHT.html
%{_javadir}/*.jar
%if %{with_gcj}
%attr(-,root,root) %{_libdir}/gcj/%{name}
%endif

%files javadoc
%defattr(0644,root,root,0755)
%doc COPYRIGHT.html
%{_javadocdir}/%{name}



%changelog

* Fri Jan 11 2013 umeabot <umeabot> 1.3.0-3.mga3
+ Revision: 350585
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Tue Nov 27 2012 ovitters <ovitters> 1.3.0-2.mga3
+ Revision: 322364
- clean spec

  + ennael <ennael>
    - Documentation group

* Fri Mar 18 2011 dmorgan <dmorgan> 1.3.0-1.mga1
+ Revision: 74306
- Really build without gcj

* Fri Mar 18 2011 ennael <ennael> 1.3.0-0.2.mga1
+ Revision: 74280
- build without gcj

* Wed Jan 26 2011 dmorgan <dmorgan> 1.3.0-0.1.mga1
+ Revision: 40180
- Adapt for mageia
- imported package flute

