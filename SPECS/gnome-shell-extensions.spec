%global major_version %%(cut -d "." -f 1 <<<%{version})
# Minimum GNOME Shell version supported
%global min_gs_version %%(cut -d "." -f 1-3 <<<%{version})

%global pkg_prefix gnome-shell-extension
%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-shell-extensions
Version:        40.7
Release:        7%{?dist}.1
Summary:        Modify and extend GNOME Shell functionality and behavior

License:        GPLv2+
URL:            http://wiki.gnome.org/Projects/GnomeShell/Extensions
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  meson
BuildRequires:  git
BuildRequires:  gettext >= 0.19.6
Requires:       gnome-shell >= %{min_gs_version}
BuildArch:      noarch

Patch001: 0001-Update-style.patch
Patch002: 0001-apps-menu-add-logo-icon-to-Applications-menu.patch
Patch003: add-extra-extensions.patch
Patch004: 0001-apps-menu-Explicitly-set-label_actor.patch
Patch005: resurrect-system-monitor.patch
Patch006: 0001-Include-top-icons-in-classic-session.patch
Patch007: 0001-desktop-icons-Update-Japanese-translation.patch
Patch008: desktop-icons-40-fixes.patch
Patch009: 0001-top-icons-Don-t-use-wm_class-as-role.patch
Patch010: 0001-heads-up-display-Add-extension-for-showing-persisten.patch
Patch011: 0001-Add-gesture-inhibitor-extension.patch
Patch012: gnome-classic-wayland.patch
Patch013: 0001-desktop-icons-Fix-stuck-grab-issue-with-rubber-bandi.patch
Patch014: window-list-touch.patch
Patch015: 0001-classification-banner-Handle-fullscreen-monitors.patch
Patch016: 0001-desktop-icons-Don-t-grab-focus-on-click.patch
Patch017: 0001-desktopManager-Hook-into-LayoutManager-to-create-gri.patch
Patch018: 0001-gesture-inhibitor-Allow-inhibiting-workspace-switch-.patch
Patch019: 0001-desktop-icons-Don-t-use-blocking-IO.patch
Patch020: 0001-window-list-Explicitly-dispose-settings-on-destroy.patch

%description
GNOME Shell Extensions is a collection of extensions providing additional and
optional functionality to GNOME Shell.

Enabled extensions:
  * apps-menu
  * auto-move-windows
  * classification-banner
  * custom-menu
  * dash-to-dock
  * desktop-icons
  * drive-menu
  * gesture-inhibitor
  * launch-new-instance
  * heads-up-display
  * native-window-placement
  * panel-favorites
  * places-menu
  * screenshot-window-sizer
  * top-icons
  * updates-dialog
  * user-theme
  * window-list
  * windowsNavigator
  * workspace-indicator


%package -n %{pkg_prefix}-common
Summary:        Files common to GNOME Shell Extensions
License:        GPLv2+
Requires:       gnome-shell >= %{min_gs_version}
Obsoletes:      %{pkg_prefix}-horizontal-workspaces < 40.0~alpha.1-3

%description -n %{pkg_prefix}-common
GNOME Shell Extensions is a collection of extensions providing additional and
optional functionality to GNOME Shell.

This package provides common data files shared by various extensions.


%package -n gnome-classic-session
Summary:        GNOME "classic" mode session
License:        GPLv2+
Requires:       %{pkg_prefix}-apps-menu = %{version}-%{release}
Requires:       %{pkg_prefix}-desktop-icons = %{version}-%{release}
Requires:       %{pkg_prefix}-launch-new-instance = %{version}-%{release}
Requires:       %{pkg_prefix}-places-menu = %{version}-%{release}
Requires:       %{pkg_prefix}-window-list = %{version}-%{release}
Requires:       nautilus

%description -n gnome-classic-session
This package contains the required components for the GNOME Shell "classic"
mode, which aims to provide a GNOME 2-like user interface.


%package -n %{pkg_prefix}-apps-menu
Summary:        Application menu for GNOME Shell
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}
Requires:       gnome-menus

%description  -n %{pkg_prefix}-apps-menu
This GNOME Shell extension adds a GNOME 2.x style menu for applications.


%package -n %{pkg_prefix}-auto-move-windows
Summary:        Assign specific workspaces to applications in GNOME Shell
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-auto-move-windows
This GNOME Shell extension enables easy workspace management. A specific
workspace can be assigned to each application as soon as it creates a window, in
a manner configurable with a GSettings key.


%package -n %{pkg_prefix}-classification-banner
Summary:        Display classification level banner in GNOME Shell
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-classification-banner
This GNOME Shell extension adds a banner that displays the classification level.


%package -n %{pkg_prefix}-custom-menu
Summary:        Add a custom menu to the desktop
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-custom-menu
This GNOME Shell extension adds a custom menu to the desktop background.


%package -n %{pkg_prefix}-dash-to-dock
Summary:        Show the dash outside the activities overview
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-dash-to-dock
This GNOME Shell extension makes the dash available outside the activities overview.


%package -n %{pkg_prefix}-desktop-icons
Summary:        Desktop icons support for the classic experience
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-desktop-icons
This GNOME Shell extension adds desktop icons support as seen in GNOME 2


%package -n %{pkg_prefix}-drive-menu
Summary:        Drive status menu for GNOME Shell
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-drive-menu
This GNOME Shell extension provides a panel status menu for accessing and
unmounting removable devices.


%package -n %{pkg_prefix}-gesture-inhibitor
Summary:        Gesture inhibitor
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-gesture-inhibitor
This GNOME Shell extension allows disabling the default desktop gestures.


%package -n %{pkg_prefix}-launch-new-instance
Summary:        Always launch a new application instance for GNOME Shell
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description  -n %{pkg_prefix}-launch-new-instance
This GNOME Shell extension modifies the behavior of clicking in the dash and app
launcher to always launch a new application instance.


%package -n %{pkg_prefix}-heads-up-display
Summary:        Display persistent on-screen message
Group:          User Interface/Desktops
License:        GPLv3+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-heads-up-display
This GNOME Shell extension displays a persistent message in the top middle of the screen.
This message can appear on the login screen, lock screen, or regular user session.


%package -n %{pkg_prefix}-native-window-placement
Summary:        Native window placement for GNOME Shell
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description  -n %{pkg_prefix}-native-window-placement
This GNOME Shell extension provides additional configurability for the window
layout in the overview, including a mechanism similar to KDE4.


%package -n %{pkg_prefix}-panel-favorites
Summary:        Favorite launchers in GNOME Shell's top bar
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-panel-favorites
This GNOME Shell extension adds favorite launchers to the top bar.


%package -n %{pkg_prefix}-places-menu
Summary:        Places status menu for GNOME Shell
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-places-menu
This GNOME Shell extension add a system status menu for quickly navigating
places in the system.


%package -n %{pkg_prefix}-screenshot-window-sizer
Summary:        Screenshot window sizer for GNOME Shell
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-screenshot-window-sizer
This GNOME Shell extension allows to easily resize windows for GNOME Software
screenshots.


%package -n %{pkg_prefix}-systemMonitor
Summary:        System Monitor for GNOME Shell
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-systemMonitor
This GNOME Shell extension is a message tray indicator for CPU and memory usage


%package -n %{pkg_prefix}-top-icons
Summary:        Show legacy icons on top
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-top-icons
This GNOME Shell extension moves legacy tray icons into the top bar


%package -n %{pkg_prefix}-updates-dialog
Summary:        Show a modal dialog when there are software updates
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-updates-dialog
This GNOME Shell extension shows a modal dialog when there are software updates


%package -n %{pkg_prefix}-user-theme
Summary:        Support for custom themes in GNOME Shell
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-user-theme
This GNOME Shell extension enables loading a GNOME Shell theme from
~/.themes/<name>/gnome-shell/.


%package -n %{pkg_prefix}-window-list
Summary:        Display a window list at the bottom of the screen in GNOME Shell
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-window-list
This GNOME Shell extension displays a window list at the bottom of the screen.


%package -n %{pkg_prefix}-windowsNavigator
Summary:        Support for keyboard selection of windows and workspaces in GNOME Shell
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-windowsNavigator
This GNOME Shell extension enables keyboard selection of windows and workspaces
in overlay mode, by pressing the Alt and Ctrl key respectively.


%package -n %{pkg_prefix}-workspace-indicator
Summary:        Workspace indicator for GNOME Shell
License:        GPLv2+
Requires:       %{pkg_prefix}-common = %{version}-%{release}

%description -n %{pkg_prefix}-workspace-indicator
This GNOME Shell extension add a system status menu for quickly changing
workspaces.


%prep
%autosetup -S git -n %{name}-%{tarball_version}


%build
%meson -Dextension_set="all" -Dclassic_mode=true
%meson_build


%install
%meson_install

%find_lang %{name}


%files -n %{pkg_prefix}-common -f %{name}.lang
%doc NEWS README.md
%license COPYING


%files -n gnome-classic-session
%{_datadir}/gnome-shell/modes/classic.json
%{_datadir}/gnome-shell/theme/*.svg
%{_datadir}/gnome-shell/theme/gnome-classic-high-contrast.css
%{_datadir}/gnome-shell/theme/gnome-classic.css
%{_datadir}/xsessions/gnome-classic.desktop
%{_datadir}/xsessions/gnome-classic-xorg.desktop
%{_datadir}/wayland-sessions/gnome-classic.desktop
%{_datadir}/wayland-sessions/gnome-classic-wayland.desktop
%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.extensions.classic.gschema.override

%files -n %{pkg_prefix}-apps-menu
%{_datadir}/gnome-shell/extensions/apps-menu*/


%files -n %{pkg_prefix}-auto-move-windows
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.auto-move-windows.gschema.xml
%{_datadir}/gnome-shell/extensions/auto-move-windows*/


%files -n %{pkg_prefix}-classification-banner
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.classification-banner.gschema.xml
%{_datadir}/gnome-shell/extensions/classification-banner*/


%files -n %{pkg_prefix}-custom-menu
%{_datadir}/gnome-shell/extensions/custom-menu*/


%files -n %{pkg_prefix}-dash-to-dock
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.dash-to-dock.gschema.xml
%{_datadir}/gnome-shell/extensions/dash-to-dock*/


%files -n %{pkg_prefix}-desktop-icons
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.desktop-icons.gschema.xml
%{_datadir}/gnome-shell/extensions/desktop-icons*/


%files -n %{pkg_prefix}-drive-menu
%{_datadir}/gnome-shell/extensions/drive-menu*/


%files -n %{pkg_prefix}-gesture-inhibitor
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.gesture-inhibitor.gschema.xml
%{_datadir}/gnome-shell/extensions/gesture-inhibitor*/


%files -n %{pkg_prefix}-launch-new-instance
%{_datadir}/gnome-shell/extensions/launch-new-instance*/


%files -n %{pkg_prefix}-heads-up-display
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.heads-up-display.gschema.xml
%{_datadir}/gnome-shell/extensions/heads-up-display*/


%files -n %{pkg_prefix}-native-window-placement
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml
%{_datadir}/gnome-shell/extensions/native-window-placement*/


%files -n %{pkg_prefix}-panel-favorites
%{_datadir}/gnome-shell/extensions/panel-favorites*/


%files -n %{pkg_prefix}-places-menu
%{_datadir}/gnome-shell/extensions/places-menu*/


%files -n %{pkg_prefix}-screenshot-window-sizer
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.screenshot-window-sizer.gschema.xml
%{_datadir}/gnome-shell/extensions/screenshot-window-sizer*/


%files -n %{pkg_prefix}-systemMonitor
%{_datadir}/gnome-shell/extensions/systemMonitor*/


%files -n %{pkg_prefix}-top-icons
%{_datadir}/gnome-shell/extensions/top-icons*/


%files -n %{pkg_prefix}-updates-dialog
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.updates-dialog.gschema.xml
%{_datadir}/gnome-shell/extensions/updates-dialog*/


%files -n %{pkg_prefix}-user-theme
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml
%{_datadir}/gnome-shell/extensions/user-theme*/


%files -n %{pkg_prefix}-window-list
%{_datadir}/gnome-shell/extensions/window-list*/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.window-list.gschema.xml


%files -n %{pkg_prefix}-windowsNavigator
%{_datadir}/gnome-shell/extensions/windowsNavigator*/


%files -n %{pkg_prefix}-workspace-indicator
%{_datadir}/gnome-shell/extensions/workspace-indicator*/


%changelog
* Thu Aug 17 2023 Florian Müllner <fmuellner@redhat.com> - 40.7-7.1
- Rebuild for custom context menu
  Resolves: #2232331

* Wed Feb 15 2023 Florian Müllner <fmuellner@redhat.com> - 40.7-7
- Fix crash on `dconf update`
  Resolves: #2170067

* Wed Jan 18 2023 Florian Müllner <fmuellner@redhat.com> - 40.7-6
- Avoid blocking IO in desktop-icons
  Resolves: #2162019

* Thu Jan 12 2023 Florian Müllner <fmuellner@redhat.com> - 40.7-5
- Add custom-menu extension
  Resolves: #2160553

* Wed Dec 14 2022 Florian Müllner <fmuellner@redhat.com> - 40.7-4
- Adjust classification banner position in fullscreen
  Resolves: #2153524
- Don't grab focus when clicking desktop grid
  Resolves: #2150001
- Make desktop icons resilient to background reloads
  Resolves: #2139895
- Allow disabling workspace switch gesture
  Resolves: #2154358

* Wed Jun 22 2022 Florian Müllner <fmuellner@redhat.com> - 40.7-3
- Improve window-list on touch
  Resolves: #2099286

* Fri May 13 2022 Florian Müllner <fmuellner@redhat.com> - 40.7-2
- Require desktop-icons for classic session
  Resolves: #2047697

* Wed Apr 13 2022 Florian Müllner <fmuellner@redhat.com> - 40.7-1
- Update to 40.7
  Resolves: #2066168

* Tue Feb 22 2022 Florian Müllner <fmuellner@redhat.com> - 40.6-1
- Update to 40.6
  Resolves: #2056410

* Tue Dec 14 2021 Florian Müllner <fmuellner@redhat.com> - 40.5-4
- Allow classification banners on lock/login screen
  Resolves: #2031186

* Tue Dec 14 2021 Florian Müllner <fmuellner@redhat.com> - 40.5-3
- Fix classification-banner preferences
  Resolves: #2031186

* Tue Dec 14 2021 Florian Müllner <fmuellner@redhat.com> - 40.5-2
- Add classification-banner
  Resolves: #2031186

* Mon Dec 13 2021 Florian Müllner <fmuellner@redhat.com> - 40.5-1
- Update to 40.5
  Resolves: #2031654

* Tue Nov 30 2021 Florian Müllner <fmuellner@redhat.com> - 40.4-8
- Fix on-screen keyboard when showing window-list
  Resolves: #2019866

* Thu Nov 18 2021 Florian Müllner <fmuellner@redhat.com> - 40.4-7
- Prevent gnome-shell from re-enabling inhibited gestures
  Resolves: #2013196

* Mon Nov 08 2021 Jonas Ådahl <jadahl@redhat.com> - 40.4-6
- Fix stuck grab on desktop-icons
  Resolves: #2019715

* Fri Oct 29 2021 Neal Gompa <ngompa@centosproject.org> - 40.4-5
- Backport GNOME Classic session for Wayland
  Resolves: #2015914

* Wed Oct 20 2021 Florian Müllner <fmuellner@redhat.com> - 40.4-4
- Adjust gesture-inhibitor extension to GNOME 40 changes
  Resolves: #2013196

* Wed Oct 20 2021 Florian Müllner <fmuellner@redhat.com> - 40.4-3
- Add gesture-inhibitor extension
  Resolves: #2013196

* Mon Sep 27 2021 Ray Strode <rstrode@redhat.com> - 40.4-2
- Add extension for displaying heads up message
  Related: #2006985

* Mon Aug 23 2021 Florian Müllner <fmuellner@redhat.com> - 40.4-1
- Update to 40.4
  Resolves: #1995095

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 40.3-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Jul 19 2021 Florian Müllner <fmuellner@redhat.com> - 40.3-1
- Update to 40.3
  Resolves: #1983551

* Tue Jun 15 2021 Florian Müllner <fmuellner@redhat.com> - 40.2-1
- Update to 40.2
  Resolves: #1971431

* Thu Jun 03 2021 Florian Müllner <fmuellner@redhat.com> - 40.1-4
- Don't use status icon wm_class as top bar role
  Resolves: #1967259

* Wed May 26 2021 Florian Müllner <fmuellner@redhat.com> - 40.1-3
- Fix various issues in downstream patches
  Resolves: #1932261

* Mon May 24 2021 Florian Müllner <fmuellner@redhat.com> - 40.1-2
- Rebase downstream patches
  Resolves: #1932261

* Mon May 17 2021 Florian Müllner <fmuellner@redhat.com> - 40.1-1
- Update to 40.1
  Resolves: #1951132

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 40.0-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Sat Mar 20 2021 Florian Müllner <fmuellner@redhat.com> - 40.0-1
- Update to 40.0

* Mon Mar 15 2021 Florian Müllner <fmuellner@redhat.com> - 40.rc-1
- Update to 40.rc

* Wed Feb 24 2021 Florian Müllner <fmuellner@redhat.com> - 40.beta-1
- Update to 40.beta

* Thu Feb 18 2021 Kalev Lember <klember@redhat.com> - 40.0~alpha.1-6.20210212git9fa522c
- Fix typo in horizontal-workspaces obsoletes package name

* Thu Feb 18 2021 Kalev Lember <klember@redhat.com> - 40.0~alpha.1-5.20210212git9fa522c
- Fix obsoletes version

* Mon Feb 15 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 40.0~alpha.1-4.20210212git9fa522c
- Add Obsoletes for horizontal-workspaces extension to fix upgrades to Fedora 34
  (RHBZ #1928415)

* Fri Feb 12 2021 Florian Müllner <fmuellner@redhat.com> - 40.0~alpha.1-3.20210212git9fa522c
- Build snapshot of current upstream
- Drop horizontal-workspaces subpackage
  (removed upstream, because horizontal workspaces are the default now)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.0~alpha.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Florian Müllner <fmuellner@redhat.com> - 40.0~alpha.1-1
- Update to 40.alpha.1

* Wed Dec 02 2020 Florian Müllner <fmuellner@redhat.com> - 40.0~alpha-1
- Update to 40.alpha

* Mon Oct 05 2020 Florian Müllner <fmuellner@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Mon Sep 14 2020 Florian Müllner <fmuellner@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Sun Sep 06 2020 Florian Müllner <fmuellner@redhat.com> - 3.37.92-1
- Update to 3.37.92

* Mon Aug 24 2020 Florian Müllner <fmuellner@redhat.com> - 3.37.91-1
- Update to 3.37.91

* Wed Aug 19 2020 Kalev Lember <klember@redhat.com> - 3.37.90-2
- Rebuild

* Tue Aug 11 2020 Florian Müllner <fmuellner@redhat.com> - 3.37.90-1
- Update to 3.37.90

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Florian Müllner <fmuellner@redhat.com> - 3.37.3-1
- Update to 3.37.3

* Wed Jun 03 2020 Florian Müllner <fmuellner@redhat.com> - 3.37.2-1
- Update to 3.37.2

* Thu Apr 30 2020 Florian Müllner <fmuellner@redhat.com> - 3.37.1-1
- Update to 3.37.1

* Tue Mar 31 2020 Florian Müllner <fmuellner@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Sat Mar 07 2020 Florian Müllner <fmuellner@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Sun Mar 01 2020 Florian Müllner <fmuellner@redhat.com> - 3.35.92-1
- Update to 3.35.92

* Tue Feb 18 2020 Florian Müllner <fmuellner@redhat.com> - 3.35.91-1
- Update to 3.35.91

* Thu Feb 06 2020 Florian Müllner <fmuellner@redhat.com> - 3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Florian Müllner <fmuellner@redhat.com> - 3.35.3-1
- Update to 3.35.3

* Wed Dec 11 2019 Florian Müllner <fmuellner@redhat.com> - 3.35.2-1
- Update to 3.35.2

* Wed Oct 09 2019 Florian Müllner <fmuellner@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Wed Sep 25 2019 Debarshi Ray <rishi@fedoraproject.org> - 3.34.0-2
- Unbreak the 'classic' GNOME session

* Mon Sep 09 2019 Florian Müllner <fmuellner@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Wed Sep 04 2019 Florian Müllner <fmuellner@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Wed Aug 21 2019 Florian Müllner <fmuellner@redhat.com> - 3.33.91-1
- Update to 3.33.91

* Sat Aug 10 2019 Florian Müllner <fmuellner@redhat.com> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Florian Müllner <fmuellner@redhat.com> - 3.33.4-1
- Update to 3.33.4

* Mon Jun 24 2019 Florian Müllner <fmuellner@redhat.com> - 3.33.3-1
- Update to 3.33.3

* Wed May 22 2019 Florian Müllner <fmuellner@redhat.com> - 3.33.2-1
- Update to 3.33.2

* Tue May 14 2019 Florian Müllner <fmuellner@redhat.com> - 3.33.1-1
- Update to 3.33.1

* Wed Apr 17 2019 Florian Müllner <fmuellner@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Tue Mar 12 2019 Florian Müllner <fmuellner@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Tue Mar 05 2019 Florian Müllner <fmuellner@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Thu Feb 21 2019 Florian Müllner <fmuellner@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Thu Feb 07 2019 Florian Müllner <fmuellner@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.31.2-2
- Fix alternate-tab extension Obsoletes tag (RHBZ #1650519)

* Wed Nov 14 2018 Florian Müllner <fmuellner@redhat.com> - 3.31.2-1
- Update to 3.31.2

* Mon Oct 08 2018 Florian Müllner <fmuellner@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Tue Sep 04 2018 Florian Müllner <fmuellner@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Mon Aug 20 2018 Florian Müllner <fmuellner@redhat.com> - 3.29.91-1
- Update to 3.29.91

* Wed Aug 01 2018 Florian Müllner <fmuellner@redhat.com> - 3.29.90-1
- Update to 3.29.90

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.29.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 24 2018 Florian Müllner <fmuellner@redhat.com> - 3.29.2-1
- Update to 3.29.2

* Fri Apr 13 2018 Florian Müllner <fmuellner@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Florian Müllner <fmuellner@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Florian Müllner <fmuellner@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Thu Feb 22 2018 Florian Müllner <fmuellner@redhat.com> - 3.27.91-1
- Update to 3.27.91

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.27.1-2
- Remove obsolete scriptlets

* Tue Oct 17 2017 Florian Müllner <fmuellner@redhat.com> - 3.27.1-1
- Update to 3.27.1

* Wed Oct 04 2017 Florian Müllner <fmuellner@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Tue Sep 12 2017 Florian Müllner <fmuellner@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Tue Aug 22 2017 Florian Müllner <fmuellner@redhat.com> - 3.25.91-1
- Update to 3.25.91

* Fri Aug 11 2017 Kevin Fenzi <kevin@scrye.com> - 3.25.90-2
- Rebuild with older working rpm

* Thu Aug 10 2017 Florian Müllner <fmuellner@redhat.com> - 3.25.90-1
- Update to 3.25.90

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Florian Müllner <fmuellner@redhat.com> - 3.25.4-1
- Update to 3.25.4

* Wed Jun 21 2017 Florian Müllner <fmuellner@redhat.com> - 3.25.3-1
- Update to 3.25.3

* Thu May 25 2017 Florian Müllner <fmuellner@redhat.com> - 3.25.2-1
- Update to 3.25.2

* Thu Apr 27 2017 Florian Müllner <fmuellner@redhat.com> - 3.25.1-1
- Update to 3.25.1

* Tue Apr 11 2017 Florian Müllner <fmuellner@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Mon Mar 20 2017 Florian Müllner <fmuellner@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Tue Mar 14 2017 Florian Müllner <fmuellner@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Wed Mar 01 2017 Florian Müllner <fmuellner@redhat.com> - 3.23.91-1
- Update to 3.23.91

* Thu Feb 16 2017 Florian Müllner <fmuellner@redhat.com> - 3.23.90-1
- Update to 3.23.90

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 23 2016 Florian Müllner <fmuellner@redhat.com> - 3.23.2-1
- Update to 3.23.2

* Tue Oct 11 2016 Florian Müllner <fmuellner@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Mon Sep 19 2016 Florian Müllner <fmuellner@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Tue Sep 13 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Tue Aug 30 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.91-1
- Update to 3.21.91

* Fri Aug 19 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.90-1
- Update to 3.21.90

* Wed Jul 20 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.4-1
- Update to 3.21.4

* Tue Jun 21 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.3-1
- Update to 3.21.3

* Fri May 27 2016 Florian Müllner <fmuellner@redhat.com> - 3.21.2-1
- Update to 3.21.2

* Tue May 10 2016 Florian Müllner <fmuellner@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 Florian Müllner <fmuellner@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Mar 16 2016 Florian Müllner <fmuellner@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Thu Mar 03 2016 Florian Müllner <fmuellner@redhat.com> - 3.19.91-1
- Update to 3.19.91

* Fri Feb 19 2016 Florian Müllner <fmuellner@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Florian Müllner <fmuellner@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Thu Dec 17 2015 Florian Müllner <fmuellner@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Wed Nov 25 2015 Florian Müllner <fmuellner@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Thu Oct 29 2015 Florian Müllner <fmuellner@redhat.com> - 3.19.1-1
- Update to 3.19.1

* Thu Oct 15 2015 Florian Müllner <fmuellner@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Florian Müllner <fmuellner@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Wed Sep 16 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Thu Sep 03 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Thu Aug 20 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.90-1
- Update to 3.17.90

* Wed Aug 19 2015 Kalev Lember <klember@redhat.com> - 3.17.4-2
- Don't own /usr/share/gnome-shell/extensions directory: now part of
  gnome-shell package

* Thu Jul 23 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.4-1
- Update to 3.17.4

* Thu Jul 02 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.3-1
- Update to 3.17.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.2-1
- Update to 3.17.2

* Fri May 01 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.1-2
- Add glib-compile-schemas rpm scripts for screenshot-window-sizer

* Thu Apr 30 2015 Florian Müllner <fmuellner@redhat.com> - 3.17.1-1
- Update to 3.17.1

* Tue Apr 14 2015 Florian Müllner <fmuellner@redhat.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Florian Müllner <fmuellner@redhat.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Florian Müllner <fmuellner@redhat.com> - 3.15.92-1
- Update to 3.15.92

* Thu Mar 05 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-2
- Obsolete the systemMonitor extension that was dropped in 3.15.91

* Thu Mar 05 2015 Florian Müllner <fmuellner@redhat.com> - 3.15.91-1
- Update to 3.15.91

* Fri Feb 20 2015 Florian Müllner <fmuellner@redhat.com> - 3.15.90-1
- Update to 3.15.90

* Wed Jan 21 2015 Florian Müllner <fmuellner@redhat.com> - 3.15.4-1
- Update to 3.15.4

* Fri Dec 19 2014 Florian Müllner <fmuellner@redhat.com> - 3.15.3.1-1
- Update to 3.15.3.1

* Fri Dec 19 2014 Florian Müllner <fmuellner@redhat.com> - 3.15.3-1
- Update to 3.15.3

* Thu Nov 27 2014 Florian Müllner <fmuellner@redhat.com> - 3.15.2-1
- Update to 3.15.2

* Thu Oct 30 2014 Florian Müllner <fmuellner@redhat.com> - 3.15.1-1
- Update to 3.15.1

* Tue Oct 14 2014 Florian Müllner <fmuellner@redhat.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Florian Müllner <fmuellner@redhat.com> - 3.14.0-1
- Update to 3.14.0

* Wed Sep 17 2014 Florian Müllner <fmuellner@redhat.com> - 3.13.92-1
- Update to 3.13.92

* Wed Sep 03 2014 Florian Müllner <fmuellner@redhat.com> - 3.13.91-1
- Update to 3.13.91

* Wed Aug 20 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.13.90-1
- Update to 3.13.90

* Thu Jul 24 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-1
- Update to 3.13.4

* Thu Jun 26 2014 Richard Hughes <rhughes@redhat.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.13.2-1
- Update to 3.13.2

* Fri May 02 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-1
- Update to 3.13.1

* Tue Mar 25 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Thu Mar 20 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.11.92-1
- Update to 3.11.92

* Thu Mar 06 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.11.91-1
- Update to 3.11.91

* Thu Feb 20 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.11.90-1
- Update to 3.11.90

* Wed Feb 05 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.11.5-1
- Update to 3.11.5

* Mon Feb 03 2014 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.11.4-1
- Update to 3.11.4

* Sun Dec 22 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.11.3-1
- Update to 3.11.3

* Wed Nov 13 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.11.2-1
- Update to 3.11.2

* Wed Oct 16 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.10.1-1
- Update to 3.10.1

* Tue Sep 24 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.10.0-1
- Update to 3.10.0

* Tue Sep 17 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.9.92-1
- Update to 3.9.92

* Tue Sep 03 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.9.91-1
- Update to 3.9.91

* Thu Aug 22 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.9.90-1
- Update to 3.9.90
- Drop xrand-indicator subpackage, no longer provided upstream

* Mon Aug 12 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.9.5-3
- Fix alternative-status-menu subpackage obsoleting

* Mon Aug 12 2013 Nils Philippsen <nils@redhat.com> - 3.9.5-2
- obsolete alternative-status-menu subpackage to allow smooth upgrades

* Sun Aug 04 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.9.5-1
- Update to 3.9.5
- Drop alternative-status-menu subpackage, no longer provided upstream

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 3.9.3-1
- Update to 3.9.3
- Obsolete default-min-max and static workspaces extensions
- Use make_install macro
- Fix bogus dates in spec changelog

* Tue May 28 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.9.2-1
- Update to 3.9.2

* Fri May 10 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.9.1-1
- Update to 3.9.1

* Fri May 10 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-3
- Obsolete gnome-applet-sensors

* Wed May 01 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-2
- Obsolete a few more fallback mode packages
- Remove gnome-panel provides

* Tue Apr 16 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Ray Strode <rstrode@redhat.com> 3.7.92-1
- Update to 3.7.92

* Tue Mar 05 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.7.91-1
- Update to 3.7.91

* Sat Mar 02 2013 Adel Gadllah <adel.gadllah@gmail.com> - 3.7.90-2
- Obsolete gnome-panel

* Fri Feb 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.90-1
- Update to 3.7.90

* Thu Feb 07 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5.1-2
- Depend on gnome-shell 3.7.5, there's no 3.7.5.1

* Thu Feb 07 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.7.5.1-1
- Update to 3.7.5
- Enable new launch-new-instance and window-list extensions, and add them in the
  classic-mode extension set
- Re-add places-menu in the classic-mode extension set

* Wed Jan 16 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.7.4-1
- Update to 3.7.4
- places-menu extension no longer part of the classic-mode extension set

* Tue Jan 01 2013 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.7.3-1
- Update to 3.7.3
- Enable new default-min-max and static-workspaces extensions
- Provide new subpackage gnome-classic-session
- Revamp summaries and descriptions

* Tue Oct 30 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.7.1-1
- Update to 3.7.1
- Drop dock and gajim extensions, no longer provided

* Tue Oct 30 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1

* Tue Oct 02 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.6.0-1
- Update to 3.6.0

* Thu Sep 06 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.5.91-1
- Update to 3.5.91

* Wed Aug 29 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.5.90-1
- Update to 3.5.90

* Sat Aug 11 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.5.5-1
- Update to 3.5.5

* Sun Jul 22 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.5.4-1
- Update to 3.5.4

* Wed Jul 18 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.5.2-1
- Update to 3.5.2
- Drop useless Provides/Obsoletes

* Sat Mar 24 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0
- Minor spec fixes

* Sat Mar 24 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.92-1
- Update to 3.3.92

* Tue Feb 28 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.90-1
- Update to 3.3.90

* Thu Feb 16 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.5-1
- Update to 3.3.5
- Spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.3.2-1
- Update to 3.3.2

* Wed Nov 30 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1
- Fix alternative-status-menu extension crash when login

* Wed Nov 09 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.0-2
- Fix dock and alternate-tab extensions
- Fix GNOME Shell version to work with GS 3.2.1

* Mon Oct 03 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Mon Sep 26 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.1.91-3.20111001gite102c0c6
- Update to a newer git snapshot
- Fix GNOME Shell version to work with GS 3.2.0
- Add Requires on GS 3.2.0 or above to gnome-shell-common

* Wed Sep 14 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.1.91-2
- Enable xrandr-indicator and workspace-indicator extensions

* Mon Sep 12 2011 Michel Salim <salimma@fedoraproject.org> - 3.1.91-1
- Update to 3.1.91
- add more documentation

* Thu Sep  1 2011 Michel Salim <salimma@fedoraproject.org> - 3.1.4-3.20110830git6b5e3a3e
- Update to git snapshot, for gnome-shell 3.1.90

* Sun Aug 21 2011 Michel Salim <salimma@fedoraproject.org> - 3.1.4-2
- Enable apps-menu extension
- Spec cleanup

* Sun Aug 21 2011 Michel Salim <salimma@fedoraproject.org> - 3.1.4-1
- Update to 3.1.4
- Enable systemMonitor extension
- Prepare xrandr-indicator, commenting out since it does not seem to work yet
- Rename subpackages in line with new guidelines (# 715367)
- Sort subpackages in alphabetical order

* Sat May 28 2011 Timur Kristóf <venemo@fedoraproject.org> - 3.0.2-1.g63dd27cgit
- Update to a newer git snapshot
- Fix RHBZ bug #708230
- Enabled systemMonitor extension, but commented out since the requirements are not available

* Fri May 13 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.1-3.03660fgit
- Update to a newer git snapshot
- Enable native-window-placement extension

* Fri May 06 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 3.0.1-2b20cbagit
- Fix description

* Thu May 5 2011 Elad Alfassa <elad@fedoraproject.org> - 3.0.1-1.b20cbagit
- Update to a newer git snapshot
- Enabled the places-menu extension

* Tue Apr 26 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.1-1.f016b9git
- Update to a newer git snapshot (post-3.0.1 release)
- Enable drive-menu extension

* Mon Apr 11 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.0.0-5.6d56cfgit
- Enable auto-move-windows extension

* Mon Apr 11 2011 Rahul Sundaram <sundaram@fedoraproject.org>  - 3.0.0-4.6d56cfgit
- Add glib2-devel as build requires

* Mon Apr 11 2011 Rahul Sundaram <sundaram@fedoraproject.org>  - 3.0.0-3.6d56cfgit
- Tweak description
- Fix typo in configure

* Mon Apr 11 2011 Rahul Sundaram <sundaram@fedoraproject.org>  - 3.0.0-2.6d56cfgit
- Added the user-theme extension
- Patch from Timur Kristóf <venemo@msn.com>

* Fri Apr 08 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 3.0.0-1.6d56cfgit
- Make sure configure doesn't get called twice

* Fri Apr 08 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 3.0.0-0.6d56cfgit
- Initial build
