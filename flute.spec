Name: flute
Version: 1.3.0
Release: 13.OOo31.0
Summary: Java CSS parser using SAC
# The entire source code is W3C except ParseException.java which is LGPLv2+
License: W3C and LGPLv2+

Source0: http://downloads.sourceforge.net/jfreereport/%{name}-%{version}-OOo31.zip
URL: http://www.w3.org/Style/CSS/SAC/
# We need to build with OpenJDK 12 because this
# is used by LibreOffice, which can't build with
# newer versions because of hsqldb 1.8.x
BuildRequires: java-12-openjdk-devel ant sac
Requires: java sac
BuildArch: noarch

%description
A Cascading Style Sheets parser using the Simple API for CSS, for Java.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
find . -name "*.jar" -exec rm -f {} \;

mkdir lib
ln -s %{_datadir}/java/sac.jar lib

%build
export JAVA_HOME=%{_prefix}/lib/jvm/java-12-openjdk
export PATH=${JAVA_HOME}/bin:${PATH}
ant jar javadoc

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/java
cp -p build/lib/%{name}.jar $RPM_BUILD_ROOT%{_datadir}/java/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_datadir}/javadoc/%{name}
cp -rp build/api $RPM_BUILD_ROOT%{_datadir}/javadoc/%{name}

%files
%defattr(0644,root,root,0755)
%doc COPYRIGHT.html
%{_datadir}/java/*.jar

%files javadoc
%defattr(0644,root,root,0755)
%doc COPYRIGHT.html
%{_datadir}/javadoc/%{name}
