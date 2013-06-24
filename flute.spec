Summary:	Java CSS parser using SAC
Name:		flute
Version:	1.3.0
Release:	1
# The entire source code is W3C except ParseException.java which is LGPLv2+
License:	W3C and LGPLv2+
Group:		System/Libraries
Url:		http://www.w3.org/Style/CSS/SAC/
Source0:	http://downloads.sourceforge.net/jfreereport/%{name}-%{version}-OOo31.zip
BuildArch:	noarch
BuildRequires:	ant
BuildRequires:	java-devel >= 0:1.6.0
BuildRequires:	jpackage-utils
BuildRequires:	sac
BuildRequires:	java-rpmbuild
Requires:	java >= 0:1.6.0 
Requires:	jpackage-utils
Requires:	sac

%description
A Cascading Style Sheets parser using the Simple API for CSS BuildRequires:	for Java.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java

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
mkdir -p %{buildroot}%{_javadir}
cp -p build/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/api %{buildroot}%{_javadocdir}/%{name}

%files
%doc COPYRIGHT.html
%{_javadir}/*.jar

%files javadoc
%doc COPYRIGHT.html
%{_javadocdir}/%{name}

