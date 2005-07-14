Summary: YUM, an rpm updater
%define name smeserver-yum
Name: %{name}
%define version 1.1.0
%define release 08
Version: %{version}
Release: %{release}
License: GPL
Group: SMEServer/addon
Source: %{name}-%{version}.tar.gz
Patch0: smeserver-yum-1.1.0.postupgrade.patch2
Patch1: smeserver-yum-1.1.0-BaseURL.patch2
Patch2: smeserver-yum-1.1.0-hideempty.patch
Patch3: smeserver-yum-1.1.0-configrepositories.patch
Patch4: smeserver-yum-1.1.0-RemovePkgPolicy.patch
Patch5: smeserver-yum-1.1.0-HandleEmptyList.patch
Patch6: smeserver-yum-1.1.0-AutoInstallUpdatesGPGCheck.patch
Patch7: smeserver-yum-1.1.0-UpdateDBs.patch
Patch8: smeserver-yum-1.1.0-systemreturn.patch
Patch9: smeserver-yum-1.1.0-CentOSdump.patch
Patch10: smeserver-yum-1.1.0-SF1216097.patch
Patch11: smeserver-yum-1.1.0-unlinktmp.patch2
Patch12: smeserver-yum-1.1.0-supervise.patch2
Patch13: smeserver-yum-1.1.0-SF1216097.patch2
Patch14: smeserver-yum-1.1.0-supervise.patch3
Patch15: smeserver-yum-1.1.0-exitstatus.patch
Patch16: smeserver-yum-1.1.0-exitstatus.patch2
Patch17: smeserver-yum-1.1.0-cronjob.patch
Patch18: smeserver-yum-1.1.0-rpm-gpg-keys
Patch19: smeserver-yum-1.1.0-import-keys.patch
Patch20: smeserver-yum-1.1.0-import-keys.patch2
Patch21: smeserver-yum-1.1.0-import-keys.patch3
Patch22: smeserver-yum-1.1.0-centos4.patch
Patch23: smeserver-yum-1.1.0-centos4.patch2
Patch24: smeserver-yum-1.1.0-updateinlocalevent.patch5
Patch25: smeserver-yum-1.1.0-signalonce.patch
Patch26: smeserver-yum-1.1.0-signalonce.patch2
Patch27: smeserver-yum-1.1.0-reponames.patch
Patch28: smeserver-yum-1.1.0-nopidcheck.patch
Patch29: smeserver-yum-1.1.0-cronjoborder.patch
Packager: Gordon Rowell <gordonr@gormand.com.au>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: yum => 1.0.3-1_73 
Requires: rpm-python => 4.0.4-7x.18
Requires: e-smith-formmagick
Requires: perl(CGI::FormMagick) >= 0.91-26
Provides: yumconf
AutoReqProv: no
%description
%name is an implementation of http://linux.duke.edu/projects/yum on SME Server

%changelog
* Thu Jul 14 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-08]
- Fix cron.daily ordering so yum_update_dbs gets a chance to fix
  the yum flag file before the standard yum cron job runs [SF: 1237639]
- Clean up various old cron jobs which are no longer used
- Change cron job template into a shell script

* Thu Jul 14 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-07]
- Remove pid file check - yum leaves stale pid files when an action
  fails, but cleans up next time. Since we're calling yum, it can
  do the work. Death to pid files.

* Thu Jul 14 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-06]
- Adjusted repository names sme{addons,core,dev,test,updates} -> 
  addons,os,dev,test,updates
- Added updates-testing
- Changed BaseURL to use mirror.contribs.org/pub/smeserver for consistency
  across mirrors
- Drop /7.0alpha/ to /7/

* Sat Jul 2 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-05]
- Fix creation of event links

* Sat Jul 2 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-04]
- Remove all other instances of services2adjust once for yum, and use
  the action script instead to avoid an endless run of yum_update_dbs

* Sat Jul 2 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-03]
- Add exec to yum service run script
- Add action script to update DBs as required, including 'local' event
- TODO: Work out why services2adjust 'once' loops forever on this service

* Sat Jul 2 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-02]
- Add Provides: yumconf [SF: 1230970]
- Cater for new yum output format, and only pick package lines from
  output [SF: 1230971]

* Thu Jun 30 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr22]
- Change from CentOS 3 to CentOS 4
- Remove force fragment for stunnel since we now ship the CentOS RPM

* Fri Jun 10 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr21]
- Import keys in bootstrap-console-save rather than post-{install,upgrade}

* Fri Jun 10 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr20]
- Populate /usr/share/rpm-gpg-keys with various RPM-GPG-KEY files
  we might want to use
- Add script to import keys
- TODO: Clean out duplicate key copies

* Thu Jun 9 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr19]
- Comment out 'once' invocation in local event - it seems to loop
- Change cron job to do the 'runsvctrl once' invocation

* Thu Jun 9 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr18]
- Fix up exit status warning.

* Thu Jun 9 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr17]
- Don't bother checking the exit status of yum, since yum may
  return non-zero for failure or for "no matching groups/packages".
  TODO: We should probably work out how to tell between these.

* Thu Jun 9 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr16]
- Make it a supervised service, but one which we only run
  "once" when we need it [SF: 1216096]

* Thu Jun 9 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr15]
- Don't try to grab the yum.pid file with Proc::PID_File as then
  we can't actually run yum commands [SF: 1216097]

* Thu Jun 9 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr14]
- Add yum_update_dbs into a supervised service so we don't have 
  to wait for it at boot time [SF: 1216096]

* Thu Jun 9 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr13]
- Unlink tmp files if yum command fails and we exit early

* Thu Jun 9 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr12]
- Check for another running yum process [SF: 1216097]
- Don't update the databases if the yum command fails [SF: 1216097]

* Fri Jun 3 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr11]
- Use the dump RPM from CentOS [SF: 1214055]

* Fri Jun 3 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr10]
- Invert exit status of system()

* Fri Jun 3 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr09]
- Move management of /var/lock/subsys/yum into yum_updates_dbs action script
- Call yum_update_dbs in local event - after the system is up and running
- Remove commented out panel references

* Fri Jun 3 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr08]
- Default gpgcheck off, except for base/updates/smecore/smeupdates
- Default yum{AutoInstallUpdates} == enabled
- Add code to manage /var/lock/subsys/yum, which controls daily updates
  in /etc/cron.daily/yum

* Fri Jun 3 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr07]
- Deal with the case when the list of updates is empty
- Put a header on each of the yum_* dbs

* Fri Jun 3 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr06]
- Rename centos repositories to match the centos-yumcache names 
- Remove pkgpolicy=last and repository ordering. 
- Add Exclude= properties to CentOS base and updates for packages which
  are modified for the SMEServer releases
- INSTALL: Need to manually remove old version of yum_repositories DB

* Fri May 31 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr05]
- Add enable/disable repository support to configuration page

* Fri May 31 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr04]
- Hide empty group/package select boxes

* Tue May 31 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr03]
- Change BaseURLs for smeserver repositories to ..../7.0alpha/ until we
  add FollowSymlinks to httpd.conf

* Fri May 27 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr02]
- Add post-upgrade configuration page
- Hide Darrell's original panels
- Remove historical event directories
- TODO: Page for adding/deleting repositories
- TODO: yum-arch local repositories

* Fri May 27 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr01]
- Roll to 1.1.0

* Fri May 27 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr30]
- Call yum_update_dbs during the actions so the db state is correct

* Fri May 27 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr29]
- Create empty yum_{available,installed,updates} dbs in SPEC file
- Display the available repositories, and provide a select box
  to allow them to be enabled/disabled.
- Add dependency on recent CGI::FormMagick so that the select options work

* Thu May 26 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr28]
- Introduce yum_repositories database and convert yum.conf template
- Introduce yum_repositories database and convert yum.conf template
- Set defaults, which can be overridden on a per-repository basis:
    yum{EnableGroups}==0
    yum{GPGCheck}==1

* Sat May 21 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr27]
- Add contrib group from CentOS and contribs.org repositories

* Fri May 20 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr26]
- Change configuration event to yum-modify since we need 
  yum-update for other purposes
- TODO: Need to update yum_* dbs after we perform an action
  so the panel status matches reality. For speed, we should
  probably delete the entries directly.
- TODO: Some yum comands take a long time, probably too long for
  the manager.
- TODO: Capture the yum output

* Fri May 20 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr25]
- Fix CGI parameter passing

* Fri May 20 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr24]
- Add actions for install/remove/update
- TODO: groupremove needs to pull apart the group and remove 
  packages individually

* Fri May 20 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr23]
- Major cleanup of yum.pm, refactoring lots of code
- Note: Depends on CGI::FormMagick patch from  [SF:1205448]

* Fri May 20 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr22]
- Changed yum{ShowPackages} to yum{PackageFunctions}
- Added enable/disable toggle to panel and fleshed out
  change_settings() so that the settings are saved
- TODO: Actually signal-event yum-update

* Fri May 20 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr21]
- Change button labels for consistency
- TODO: Deal with degenerate case where no groups exist

* Fri May 20 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr20]
- Show groups in the panel
- Hide the ability to install/remove individual packages by default
- To enable, set yum{ShowPackages}=yes
- Add a tst group, courtesy of Greg Swallow

* Fri May 20 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr19]
- List available/installed/updates for yum groups as well
- Create yum_installed db and use that instead of /var/log/rpmpkgs
  for orthogonality. We also update all three DBs with one action.

* Fri May 20 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr18]
- enablegroups for smeserver, but disable them for centos

* Fri May 20 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr17]
- For consistency, sort extras before os as well

* Fri May 20 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr16]
- Set pkgpolicy=last, put centos groups before smeserver groups, and
  ensure that the group labels are sortable

* Thu May 19 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr15]
- Comment out the smeserver parts of yum.conf for now

* Thu May 19 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr14]
- Fill in removable packages from /var/log/rpmpkgs, updated nightly
  by a cronjob in the rpm package. 
  TODO: We should probably run the cron job just before displaying 
  this panel

* Thu May 19 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr13]
- Rough in install/remove pages

* Thu May 19 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr12]
- Add configuration page to panel

* Thu May 19 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr11]
- Fix up conf-yum and /etc/yum.conf links

* Thu May 19 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr10]
- Clean up daily cronjobs, and check whether yum is enabled in each of them
- Remove /var/service/yum - we don't need to run all the time
- Make use of new templates.metadata to remove conf-yum script entirely

* Thu May 19 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr09]
- Rewrite yum.conf templates to depend on:
  sysconfig{ReleaseVersion}
  sysconfig{BaseDistro}
  sysconfig{BaseDistroVersion}

* Fri May 13 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr08]
- Initial FormMagick panel using new databases

* Fri May 13 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr07]
- And put yum_update_dbs in the right directory...

* Fri May 13 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr06]
- Add /sbin/e-smith/yum_update_dbs

* Fri May 13 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr05]
- Change db names and fix yum list updates command

* Fri May 13 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr04]
- Generate esmith::DB files from the yum output, as it's so much
  easier to deal with them later in panels, etc.

* Fri May 13 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr03]
- Change output path of yum list commands

* Fri May 13 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr02]
- Fix up init.d/supervise/yum symlink
- Create /service symlink
- Ensure correct permissions on supervise bits and pieces

* Fri May 13 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-04gr01]
- Change default type for yum to service
- Add yum{status}==enabled
- Create /var/log/yum in build
- Add yum service directory and startup

* Mon Mar 01 2004 Darrell May <dmay@myezserver.com>
- [1.0.0-03dmay]
- bugfix to yum-config missing db set {Arch,Check}Repository
* Sun Feb 29 2004 Darrell May <dmay@myezserver.com>

- [1.0.0-02dmay]
- major updates to yum panels, templates
* Sun Feb 08 2004 Darrell May <dmay@myezserver.com>

- [1.0.0-01_beta]
- initial beta release
- added yum-remove panel
- updated all panels, events, actions
* Sat Feb 07 2004 Darrell May <dmay@myezserver.com>

- [0.0.1a-09]
- added yum-post panel
- updated yum-{update,available} panels
- updated yum-install-{available,update} events & actions

* Tue Feb 03 2004 Darrell May <dmay@myezserver.com>
- [0.0.1a-08]
- added pre-alpha yum-{update,available} panels
- renamed all panels yum-panelname

* Mon Feb 02 2004 Darrell May <dmay@myezserver.com>
- [0.0.1a-07]
- updated yum-check-repository template and action to accept --nomail commandline option
- updated yumcheck panel to issue --nomail commandline option

* Sun Feb 01 2004 Darrell May <dmay@myezserver.com>
- [0.0.1a-06]
- added yumcheck server-manager panel
- updated cron.daily/yum-check-repository template
- change log file name to yum-check-repository.log

* Sat Jan 31 2004 Darrell May <dmay@myezserver.com>
- [0.0.1a-05]
- added yumconfig server-manager panel
- added yum-post-{install,remove} events
- added navigation-conf-hidden action

* Mon Jan 26 2004 Darrell May <dmay@myezserver.com>
- [0.0.1a-04]
- moved cron.hourly actions to cron.daily
- added yum-update event
- added yum-arch-repository yum-check-repository actions
- added yum-install-updates yum-install-available actions
- removed %post entries, created db defaults

* Sun Jan 25 2004 Darrell May <dmay@myezserver.com>
- [0.0.1a-03]
- yum-check-repository, changed to run 'yum list'
- yum-arch-repository, added support for multiple archive repositories

* Sat Jan 24 2004 Darrell May <dmay@myezserver.com>
- [0.0.1a-02]
- fix db typo UpdateURL to UpdatesUrl
- added cron.hourly/yum-check-repository & yum-arch-repository
- updated actions/conf-yum

* Thu Jan 22 2004 Darrell May <dmay@myezserver.com>
- [0.0.1a-01]
- Original version

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1

rmdir root/etc/e-smith/events/yum-post-install
rmdir root/etc/e-smith/events/yum-install-updates
rmdir root/etc/e-smith/events/yum-install-available

%build
perl createlinks

mkdir -p root/service
ln -s /var/service/yum root/service/yum
mkdir -p root/var/service/yum/supervise
touch root/var/service/yum/down
mkdir -p root/var/service/yum/log/supervise
mkdir -p root/var/log/yum

mkdir -p root/etc/e-smith/db/yum_{available,installed,updates}

%install
/bin/rm -rf $RPM_BUILD_ROOT
(cd root   ; /usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)
/bin/rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist \
    --file '/sbin/e-smith/yum_update_dbs' 'attr(0700,root,root)' \
    --file '/etc/cron.daily/smeserver-yum' 'attr(0700,root,root)' \
    --file /var/service/yum/down 'attr(0644,root,root)' \
    --file /var/service/yum/run 'attr(0755,root,root)' \
    --dir /var/service/yum/log 'attr(0755,root,root)' \
    --dir /var/service/yum/log/supervise 'attr(0700,root,root)' \
    --dir /var/service/yum/supervise 'attr(0700,root,root)' \
    --file /var/service/yum/log/run 'attr(0755,root,root)' \
    --dir /var/log/yum 'attr(2750,smelog,smelog)' \
    $RPM_BUILD_ROOT > %{name}-%{version}-%{release}-filelist

%clean
/bin/rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist

%defattr(-,root,root)

%preun

%postun

%pre

%post
rm -f /etc/cron.daily/yum-arch-repository
rm -f /etc/cron.daily/yum-check-repository
rm -f /etc/cron.daily/yum-update-dbs
