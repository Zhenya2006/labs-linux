Name:           count-etc-files
Version:        1.0
Release:        1%{?dist}
Summary:        Bash script that counts regular files in /etc

License:        GPL
BuildArch:      noarch

%description
Simple bash script that counts regular files in /etc excluding directories and symbolic links.

%prep

%build

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 755 %{_sourcedir}/count_files.sh %{buildroot}/usr/local/bin/count_files.sh

%files
/usr/local/bin/count_files.sh

%changelog
* %(date +"%a %b %d %Y") Yevhen Tarasovych - 1.0-1
- Initial RPM package
