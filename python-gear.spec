%global owner openstack-infra
%global srcname gear

Name:      python-%{srcname}
Version:   0.11.0
Release:   1%{?dist}
Summary:   Pure Python Async Gear Protocol Library

Group:     Applications/Productivity
License:   ASL 2.0
URL:       https://github.com/openstack-infra/%{srcname}
Source0:   https://github.com/openstack-infra/gear/archive/%{version}.tar.gz

BuildArch: noarch

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-pbr

Requires: python-extras
Requires: python-argparse
Requires: python-daemon
Requires: python-pbr


%description
python-gear implements an asynchronous event-driven interface to Gearman.
It provides interfaces to build a client or worker, and access to the
administrative protocol. The design approach is to keep it simple, with a
relatively thin abstraction of the Gearman protocol itself. It should be
easy to use to build a client or worker that operates either synchronously
or asynchronously. The module also provides a simple Gearman server for
use as a convenience in unit tests. The server is not designed for
production use under load.


%prep
%setup -qn %{srcname}-%{version}
rm -f requirements.txt


%build
PBR_VERSION=%{version} %{__python} setup.py build


%install
PBR_VERSION=%{version} %{__python} setup.py install --skip-build --root %{buildroot}


%files
%doc README.rst CONTRIBUTING.rst doc
%license LICENSE
%{_bindir}/*
%{python_sitelib}/%{srcname}
%{python_sitelib}/%{srcname}-*egg-info


%changelog
* Tue Jan 30 2018 Fabien Boucher <fboucher@redhat.com> - 0.11.0-1
- Bump to 0.11.0

* Sat May 20 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 0.9.1-1
- Bump to 0.9.1

* Tue Apr 11 2017 Tristan Cacqueray <tdecaqu@redhat.com> - 0.5.8-2
- Add python-setuptool build requirement

* Mon Jun 22 2015 Fabien Boucher <fboucher@redhat.com> - 0.5.8-1
- Bump gear source to version 0.5.8
- Add python-pbr as dependency as demo geard needs it

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Fabien Boucher <fboucher@redhat.com> - 0.5.7-1
- Bump gear source to version 0.5.7
- Remove dist version in changelog
- Fix license handling

* Thu Apr 23 2015 Fabien Boucher <fboucher@redhat.com> - 0.5.6-0
- Initial packaging
