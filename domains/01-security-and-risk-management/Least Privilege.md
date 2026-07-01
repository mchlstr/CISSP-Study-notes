# Least Privilege

## Overview

Least privilege means every subject — user, process, or system — gets only the access its job requires, and nothing more. The point is to shrink the **blast radius**: if an account is phished or a service is exploited, the attacker inherits exactly that account's rights, so the less it can touch, the less damage a compromise can do. A help-desk clerk who can reset passwords but not read payroll, or a web service that can query one database table but not drop it, both limit how far one breach can spread. It's the default-deny mindset applied to permissions: start at zero and add only what's justified.

## Applications
- **User accounts** - grant only needed permissions
- **Service accounts** - restrict to required resources
- **Applications** - run with minimum OS-level permissions
- **Network access** - limit to necessary segments
- **Database access** - restrict to needed tables/views
- **Administrative access** - use regular accounts for daily work; elevate only when needed

## Related Concepts
- **Need to Know** - access to specific information only when justified
- **Just-in-Time Access** - provision access on demand, revoke after use
- **Privilege Creep** - gradual accumulation of unnecessary access over time (prevented by access reviews)

## Exam Tips

- Least privilege limits the **damage** of a compromised account; separation of duties limits what one person can do **on purpose**.
- **Common trap — least privilege vs. need-to-know:** least privilege governs *what you can do* (permissions/actions); need-to-know governs *what data you can see*. They overlap but aren't synonyms — watch which the question is testing.
- **Privilege creep** is the classic failure mode; the fix is periodic **access recertification/reviews**, not just careful provisioning.
- "Run with minimum required rights" and "elevate only when needed" (just-in-time) are least-privilege answers.

## Related Topics

- [Separation of Duties](Separation%20of%20Duties.md)
- [Access Control Models](../05-identity-and-access-management/Access%20Control%20Models.md)
- [Personnel Security](../01-security-and-risk-management/Personnel%20Security.md)
- [Secure Design Principles](../03-security-architecture-and-engineering/Secure%20Design%20Principles.md)
- [Identity Management](../05-identity-and-access-management/Identity%20Management.md) - enforcing through provisioning
