# Generated from unf_ext-0.0.7.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name unf_ext

Name: rubygem-%{gem_name}
Version: 0.0.7.4
Release: 2%{?dist}
Summary: CRuby library for Unicode Normalization Form
Group: Development/Languages
License: MIT
URL: https://github.com/knu/ruby-unf_ext
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: gcc-c++ 
# BuildRequires: rubygem(test-unit)
# BuildRequires: rubygem(rake-compiler) >= 0.7.9
# BuildRequires: rubygem(rake-compiler-dock) >= 0.6.0
# BuildRequires: rubygem(rake-compiler-dock) < 0.7


Provides: rubygem(%{gem_name}) = %{version}

%description
Unicode Normalization Form support library for CRuby.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_libdir}/unf_ext.so %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/



# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_instdir}/unf_ext.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/.document
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Tue Jun 20 2017 Juan Badia Payno <jbadiapa@redhat.com> - 0.0.7.4-2
- Centos Package

* Wed Apr 19 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.4-1
- 0.0.7.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.2-4
- F-26: rebuild for ruby24

* Fri Sep  2 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.2-3
- Explicitly mark C-type char array as signed char, ppc defaults char
  to unsigned as well as arm

* Sat Feb  6 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.2-2
- F-24(C++14): pass -Wno-narrowing for now on arm due to char
  being unsigned by default and narrowing initializer issue

* Fri Feb  5 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.2-1
- 0.0.7.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.1-3
- F-24: rebuild against ruby23

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.1-1
- 0.0.7.1

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.6-8
- F-22: Rebuild for ruby 2.2

* Fri Nov 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.6-7
- F-21 shoulda is now 3.5.0, fix test case

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.6-4
- Use minitest/autorun instead of minitest/unit

* Tue Apr 22 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.6-3
- F-21: rebuild for ruby 2.1 / rubygems 2.2

* Wed Sep 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.6-2
- Misc fix

* Fri Mar 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.6-1
- 0.0.6
- Support new ruby packaging guideline

* Sun Jan 06 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.5-1
- Initial package

